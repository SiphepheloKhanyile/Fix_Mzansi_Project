"""
User Aunthentication Views Module
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSettingsForm
from .forms import CustomPasswordChangeForm


def signin_view(request):
    """
    Sign In View
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a success page.
        else:
            messages.error(request, 'Incorrect username or password.')

    return render(request, 'user_auth/signin.html')


def signup_view(request):
    """
    Sign Up View
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())  # Login registered user
            return redirect('home')  # Redirect to the Home page.
    else:
        form = UserCreationForm()

    return render(request, 'user_auth/signup.html', {'form': form})


def logout_view(request):
    """
    Logout View
    """
    logout(request)
    return redirect('home')


@login_required(login_url='/user/signin/')
def user_settings(request):
    """
    Combined User Profile Settings and Password Change View
    """
    if request.method == 'POST':

        if 'user_settings_submit' in request.POST:
            # if user clicked change profile form button
            profile_form =\
                UserSettingsForm(request.POST, instance=request.user)

            password_form = CustomPasswordChangeForm(request.user)

            # Check if both forms are valid
            if profile_form.is_valid():
                # Save profile changes
                profile_form.save()
                return redirect('profile')

        if 'password_change_submit' in request.POST:
            # if user clicked change password form button
            password_form =\
                CustomPasswordChangeForm(request.user, request.POST)

            profile_form = UserSettingsForm(instance=request.user)

            if password_form.is_valid():
                # Save password change and login user
                # (if the password fields are not empty)
                if password_form.cleaned_data['old_password'] and\
                   password_form.cleaned_data['new_password1']:
                    login(request, password_form.save())

                # Redirect to the profile page
                return redirect('profile')
    else:
        # Initialize both forms with the current user instance
        profile_form = UserSettingsForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)

    # Render the template with both forms
    return render(request, 'user_auth/profile.html',
                  {'form': profile_form, 'pass_form': password_form,
                   'title': 'Profile'})
