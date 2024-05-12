"""
Database Models
"""
from django.db import models
from django.contrib.auth.models import User


class LogIssue(models.Model):
    """
    Issues Database Model
    """
    ISSUE_CATEGORIES = [
        ('INF', 'Infrastructure'),
        ('ENV', 'Environmental'),
        ('SAF', 'Safety'),
        ('SOC', 'Social'),
        ('ECO', 'Economic'),
        ('EDU', 'Educational'),
        ('HEA', 'Health'),
        ('OTH', 'Other'),
    ]

    issue_title = models.CharField(max_length=255)
    issue_description = models.TextField()
    street_name = models.CharField(max_length=255, blank=True, null=True)
    city_name = models.CharField(max_length=255, blank=True, null=True)
    town_name = models.CharField(max_length=255, blank=True, null=True)
    suburb_name = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    state_name = models.CharField(max_length=100)
    address_type = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=3, choices=ISSUE_CATEGORIES, default='OTH')  # noqa: E501

    class Meta:
        """
        table configs
        """
        db_table = 'log_issue'

    def __str__(self):
        """
        String representation of object
        """
        return f"{self.issue_title} - {self.city_name}, {self.suburb_name}"


class Media(models.Model):
    """
    Logged Issue Media attatchments models
    """
    log_issue =\
        models.ForeignKey(LogIssue, related_name='media', on_delete=models.CASCADE)  # noqa: E501
    file = models.FileField(upload_to='uploads/')

    class Meta:
        """
        table configs
        """
        db_table = 'media_files'

    def __str__(self):
        """
        String representation of object
        """
        return f"{self.log_issue} - Media Upload"
