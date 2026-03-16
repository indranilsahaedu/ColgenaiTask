from django import forms
from .models import Campaign


class CampaignForm(forms.ModelForm):

    class Meta:

        model = Campaign

        fields = [
            "campaign_name",
            "subject_line",
            "email_content",
            "scheduled_time"
        ]

        widgets = {

            "scheduled_time": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),

            "email_content": forms.Textarea(
                attrs={"rows": 6}
            ),
        }


class RecipientUploadForm(forms.Form):

    file = forms.FileField()