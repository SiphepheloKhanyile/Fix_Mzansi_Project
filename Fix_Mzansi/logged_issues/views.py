"""
Logged Issues view Module
"""
from django.shortcuts import render
from log_issue.models import LogIssue


def logged_issues_view(request):
    """
    For Logged Issues Map
    """
    issues = LogIssue.objects.all()
    return render(request, 'logged_issues/logged_issues.html',
                  {'issues': issues, 'title': "Logged Issues"})
