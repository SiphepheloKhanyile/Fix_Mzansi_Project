"""
User Auth Forms Module
"""
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm

User = get_user_model()


class UserSettingsForm(UserChangeForm):
    """
    User Profile Form
    """
    class Meta:
        """
        defining fields to show on form
        """
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    Custom Password Change Form
    """
    class Meta:
        """
        Defining fields to show on form
        """
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
