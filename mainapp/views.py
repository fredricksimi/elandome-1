from django.shortcuts import redirect, render
from .forms import ContactPageForm, VolunteerApplicationForm
from datetime import datetime, timezone
from django.utils.translation import gettext as _
from django.contrib import messages
# Create your views here.

def home_view(request):
    active = 'active'
    context = {'active':active}
    return render(request, 'mainapp/index.html', context)

def about_view(request):
    active = 'active'
    context = {'active':active}
    return render(request, 'mainapp/about.html', context)

def history_view(request):
    return render(request, 'mainapp/history.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactPageForm(request.POST or None)
        if form.is_valid():
            form.save()
            redirect('mainapp:contact')
            messages.success(request, 'Your details were submitted successfully!')
            form = ContactPageForm()
        else:
            messages.warning(request, 'Please correct the errors below.')
    else:
        form = ContactPageForm()
    active = 'active'
    context = {
        'active':active,
        'form':form
        }
    return render(request, 'mainapp/contact.html', context)

def portfolio_view(request):
    active = 'active'
    context = {'active':active}
    return render(request, 'mainapp/portfolio.html', context)

def programs_view(request):
    active = 'active'
    context = {'active':active}
    return render(request, 'mainapp/programs.html', context)

def edc_community_view(request):
    return render(request, 'mainapp/edc-community.html')

def services_view(request):
    active = 'active'
    context = {'active':active}
    return render(request, 'mainapp/services.html', context)

def application_view(request):
    if request.method == 'POST':
        form = VolunteerApplicationForm(request.POST or None)
        if form.is_valid():
            form.save()
            redirect('mainapp:application-form')
            messages.success(request, 'Your details were submitted successfully!')
            form=VolunteerApplicationForm()
        else:
            messages.warning(request, 'Please correct the errors below.')
    else:
        form = VolunteerApplicationForm()
    active = 'active'
    context = {
        'active':active,
        'form':form
    }
    return render(request, 'mainapp/application-form.html', context)

def news_view(request):
    return render(request, 'mainapp/news.html')

def gallery_view(request):
    return render(request, 'mainapp/gallery.html')

def events_view(request):
    return render(request, 'mainapp/events.html')