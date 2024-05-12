"""
views module
Contains backend logic for home("/") app route
"""

from django.shortcuts import render
from log_issue.models import LogIssue


# Create your views here.
def home(request):
    """
    Home Page View
    """
    query = request.GET.get('q')
    if query:
        issues = LogIssue.objects.filter(state_name__icontains=query)
    else:
        issues = LogIssue.objects.all()
    # issues = LogIssue.objects.all()
    return render(request, 'home/home.html',
                  {'issues': issues,
                   'title': 'Home',
                   'request_user': request.user})
