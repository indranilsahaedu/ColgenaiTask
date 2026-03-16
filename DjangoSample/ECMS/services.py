import csv
import os
from django.core.mail import EmailMessage

from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from .models import Campaign, Recipient, DeliveryLog
from datetime import timedelta


def run_scheduled_campaigns():
    print("Checking campaigns...")

    from django.utils import timezone

    now = timezone.localtime()

    print("Local Time:", now)


    campaigns = Campaign.objects.filter(
        status="Scheduled",
        scheduled_time__lte=now
    )
    print(campaigns)
    for campaign in campaigns:

        recipients = Recipient.objects.filter(
            subscription_status="Subscribed"
        )

        campaign.status = "In Progress"
        print("In Progress")
        campaign.save()

        sent = 0
        failed = 0

        for user in recipients.iterator():

            try:

                send_mail(
                    campaign.subject_line,
                    campaign.email_content,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False
                )

                DeliveryLog.objects.create(
                    campaign=campaign,
                    recipient_email=user.email,
                    status="Sent"
                )

                sent += 1

            except Exception as e:

                DeliveryLog.objects.create(
                    campaign=campaign,
                    recipient_email=user.email,
                    status="Failed",
                    failure_reason=str(e)
                )

                failed += 1

        campaign.sent_count = sent
        campaign.failed_count = failed
        campaign.status = "Completed"
        print("Completed")
        campaign.save()
        send_campaign_report(campaign)



def send_campaign_report(campaign):

    logs = DeliveryLog.objects.filter(campaign=campaign)

    filename = f"campaign_report_{campaign.id}.csv"

    filepath = os.path.join("media", filename)

    os.makedirs("media", exist_ok=True)

    with open(filepath, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Recipient Email",
            "Status",
            "Failure Reason",
            "Sent At"
        ])

        for log in logs:

            writer.writerow([
                log.recipient_email,
                log.status,
                log.failure_reason,
                log.sent_at
            ])

    email = EmailMessage(
        subject=f"Campaign Report: {campaign.campaign_name}",
        body=f"""
Campaign Completed

Campaign Name: {campaign.campaign_name}

Total Sent: {campaign.sent_count}
Total Failed: {campaign.failed_count}

See attached CSV report.
""",
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.ADMIN_REPORT_EMAIL],
    )

    email.attach_file(filepath)

    email.send()