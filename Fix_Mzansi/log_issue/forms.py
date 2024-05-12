"""
Model Forms Module
"""
from django import forms
from .models import LogIssue, Media


class LogIssueForm(forms.ModelForm):
    """
    Form to Log an Issue
    """
    # city_name = forms.CharField(disabled=True)
    # town_name = forms.CharField(disabled=True)
    # suburb_name = forms.CharField(disabled=True)
    # street_name = forms.CharField(disabled=True)
    # state_name = forms.CharField(disabled=True)
    # municipality = forms.CharField(disabled=True)
    # latitude = forms.CharField(disabled=True)
    # longitude = forms.CharField(disabled=True)
    # address_type = forms.CharField(disabled=True)

    class Meta:
        """
        defining fields to show on form
        """
        model = LogIssue
        fields = ['issue_title', 'issue_description', 'street_name',
                  'city_name', 'town_name', 'suburb_name', 'municipality',
                  'state_name', 'address_type', 'latitude', 'longitude',
                  'category'
                  ]


class MediaForm(forms.ModelForm):
    """
    Media Form for the Issue
    """
    class Meta:
        """
        defining fields to show on form
        """
        model = Media
        fields = ['file']
