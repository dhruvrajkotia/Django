from django.shortcuts import render, redirect
from .models import Meetup, Participent
from .forms import RegistrationForms

# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', { 
        "meetups":meetups
        })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registation_form = RegistrationForms()
        else: 
            registation_form = RegistrationForms(request.POST)
            if registation_form.is_valid():
                user_email = registation_form.cleaned_data['email']
                participant, _ = Participent.objects.get_or_create(email=user_email)
                selected_meetup.participents.add(participant)
                return redirect('confirm-registration')
        
        return render(request, 'meetups/meetup-details.html', 
            {
                'meetup': selected_meetup,
                'meetup_found': True,
                'form': registation_form
            })


    except Exception as e: 
        print(e)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })


def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')