"""
Tags to determine if user is on which url
and place border around it
"""
from django import template
from django.urls import resolve

register = template.Library()


@register.simple_tag
def active(request, view_name):
    """
    Active Link Tag
    """
    return 'active' if resolve(request.path).view_name == view_name else ''
