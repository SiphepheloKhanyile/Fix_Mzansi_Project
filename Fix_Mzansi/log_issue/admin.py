"""
For /admin puroses
"""
from django.contrib import admin
from .models import LogIssue, Media


@admin.register(LogIssue)
class LogIssueAdmin(admin.ModelAdmin):
    """
    Register the LogIssue model
    """
    list_display =\
        ('issue_title', 'city_name', 'suburb_name', 'date_posted', 'updated_at', 'posted_by')  # noqa: E501
    search_fields = ('issue_title', 'city_name', 'suburb_name')
    list_filter = ('date_posted', 'updated_at')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    """
    Register the Media model
    """
    list_display = ('log_issue', 'file')
    search_fields = ('log_issue__issue_title',)
    list_filter = ('log_issue__date_posted',)
