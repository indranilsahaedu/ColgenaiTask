from django.db import models


class Recipient(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    subscription_status = models.CharField(
        max_length=20,
        default="Subscribed"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Campaign(models.Model):

    STATUS = (
        ("Draft", "Draft"),
        ("Scheduled", "Scheduled"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    )

    campaign_name = models.CharField(max_length=200)

    subject_line = models.CharField(max_length=200)

    email_content = models.TextField()

    scheduled_time = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Draft"
    )

    sent_count = models.IntegerField(default=0)

    failed_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_recipients(self):

        return Recipient.objects.filter(
            subscription_status="Subscribed"
        ).count()

    def __str__(self):
        return self.campaign_name


class DeliveryLog(models.Model):

    STATUS = (
        ("Sent", "Sent"),
        ("Failed", "Failed"),
    )

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE
    )

    recipient_email = models.EmailField()

    status = models.CharField(
        max_length=10,
        choices=STATUS
    )

    failure_reason = models.TextField(
        blank=True,
        null=True
    )

    sent_at = models.DateTimeField(auto_now_add=True)