from django.urls import path
from . import views

app_name='mainapp'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('history', views.history_view, name='history'),
    path('contact', views.contact_view, name='contact'),
    path('portfolio', views.portfolio_view, name='portfolio'),
    path('programs', views.programs_view, name='programs'),
    path('edc-community', views.edc_community_view, name='edc-community'),
    path('services', views.services_view, name='services'),
    path('apply', views.application_view, name='application-form'),
    path('news', views.news_view, name='news'),
    path('gallery', views.gallery_view, name='gallery'),
    path('events', views.events_view, name='events'),
    path('resources', views.resources_view, name='resources')
]