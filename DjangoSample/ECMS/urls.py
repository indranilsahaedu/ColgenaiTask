from django.urls import path
from . import views

urlpatterns = [

    path("", views.dashboard, name="dashboard"),

    path(
        "create/",
        views.create_campaign,
        name="create_campaign"
    ),

    path(
        "upload/",
        views.upload_recipients,
        name="upload_recipients"
    ),

    path(
        "campaign/<int:id>/",
        views.campaign_detail,
        name="campaign_detail"
    ),
    path(
        "campaign/delete/<int:id>/",
        views.delete_campaign,
        name="delete_campaign"
    ),
    path("ajax/campaigns/", views.ajax_campaigns, name="ajax_campaigns"),
]