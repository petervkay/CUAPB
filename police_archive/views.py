from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import Officer, Incident
from .forms import SearchForm

def search(request):
    form = SearchForm(request.GET)
    officers = form.search()
    return render_to_response('police_archive/search.html', {'officers': officers})

def index(request):
	officer_list = Officer.objects.order_by('last_name')
	
	context= {
		'officer_list': officer_list,
	}
	return render(request, 'police_archive/index.html', context)

def officer(request, officer_badge):
    return HttpResponse("You're looking at the officer with badge #%s." % officer_badge)

def incident(request, case_number):
    return HttpResponse("You're looking at incident %s." % case_number)


