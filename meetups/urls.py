from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all-meetups'),
    path('success/', views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>/', views.meetup_details, name='meetup-detail'), # our-domain.com/meetups/<dynamic-path-segment>
]
