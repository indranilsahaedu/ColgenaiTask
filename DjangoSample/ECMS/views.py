import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone

from .models import Campaign, Recipient, DeliveryLog
from .forms import CampaignForm, RecipientUploadForm
from .services import run_scheduled_campaigns


def dashboard(request):

    # run_scheduled_campaigns()

    campaigns = Campaign.objects.all().order_by("-created_at")

    return render(
        request,
        "dashboard.html",
        {"campaigns": campaigns}
    )
def ajax_campaigns(request):

    campaigns = Campaign.objects.all().order_by("-created_at")

    return render(
        request,
        "partials/campaign_table.html",
        {"campaigns": campaigns}
    )

def create_campaign(request):

    if request.method == "POST":

        form = CampaignForm(request.POST)

        if form.is_valid():

            campaign = form.save(commit=False)

            if campaign.scheduled_time <= timezone.now():

                campaign.status = "In Progress"

            else:

                campaign.status = "Scheduled"

            campaign.save()

            messages.success(request, "Campaign Created")

            return redirect("dashboard")

    else:

        form = CampaignForm()

    return render(
        request,
        "create_campaign.html",
        {"form": form}
    )


def upload_recipients(request):

    if request.method == "POST":

        form = RecipientUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            file = request.FILES["file"]

            decoded = file.read().decode("utf-8").splitlines()

            reader = csv.DictReader(decoded)

            for row in reader:

                if not Recipient.objects.filter(
                        email=row["email"]).exists():

                    Recipient.objects.create(
                        name=row["name"],
                        email=row["email"]
                    )

            messages.success(request, "Recipients Uploaded")

            return redirect("dashboard")

    else:

        form = RecipientUploadForm()

    return render(
        request,
        "upload_recipients.html",
        {"form": form}
    )


def campaign_detail(request, id):

    campaign = get_object_or_404(Campaign, id=id)

    logs = DeliveryLog.objects.filter(campaign=campaign)

    return render(
        request,
        "campaign_detail.html",
        {"campaign": campaign, "logs": logs}
    )

def delete_campaign(request, id):

    campaign = get_object_or_404(Campaign, id=id)

    campaign.delete()

    messages.success(request, "Campaign deleted successfully")

    return redirect("dashboard")