"""
views module
Contains backend logic for logging issues("/log_issue") app route
"""
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import LogIssueForm, MediaForm
from .models import LogIssue, Media  # noqa: F401


@login_required(login_url='/user/signin/')
def log_issue_view(request):
    """
    Log Issue View
    """
    if request.method == 'POST':
        log_issue_form = LogIssueForm(request.POST)
        media_form = MediaForm(request.POST, request.FILES)

        if log_issue_form.is_valid() and media_form.is_valid():
            log_issue = log_issue_form.save(commit=False)
            log_issue.posted_by = request.user  # Assuming the user is logged in  # noqa: E501
            log_issue.save()

            media = media_form.save(commit=False)
            media.log_issue = log_issue
            media.save()

            return redirect('home')  # Redirect to a success page

    else:
        log_issue_form = LogIssueForm()
        media_form = MediaForm()

    context = {
        'log_issue_form': log_issue_form,
        'media_form': media_form,
        'title': "Log Issue"
    }

    return render(request, 'log_issue/post_issue.html', context=context)


@login_required(login_url='/user/signin/')
def update_issue(request, post_id):
    """
    Update Issue View
    """
    issue = get_object_or_404(LogIssue, id=post_id)
    # media = get_object_or_404(Media, file=issue.file)
    media_instance, created = Media.objects.get_or_create(log_issue=issue)
    if request.method == 'POST':
        if 'profile_form_button' in request.POST:
            form = LogIssueForm(request.POST, instance=issue)
            media_form =\
                MediaForm(request.POST, request.FILES, instance=media_instance)

            if form.is_valid():
                form.save()
                messages.success(request, 'Issue updated successfully.')
                return redirect('update_issue', post_id=post_id)

        if 'media_form_button' in request.POST:
            form = LogIssueForm(instance=issue)
            media_form =\
                MediaForm(request.POST, request.FILES, instance=media_instance)
            if media_form.is_valid():
                media_form.save()
                messages.success(request, 'Media updated successfully.')
                return redirect('update_issue', post_id=post_id)
    else:
        form = LogIssueForm(instance=issue)
        media_form = MediaForm(instance=media_instance)

    context = {
        'log_issue_form': form,
        'media_form': media_form,
        'title': "Update Issue",
        # 'media': media
    }
    return render(request, 'log_issue/update_issue.html', context=context)


@login_required(login_url='/user/signin/')
def delete_issue(request, post_id):
    """
    Update Issue View
    """
    issue = get_object_or_404(LogIssue, id=post_id)
    if request.method == 'POST':
        issue.delete()
        messages.success(request, 'Issue deleted successfully.')
        return redirect('home')
    return render(request, 'delete_issue.html', {'issue': issue})
