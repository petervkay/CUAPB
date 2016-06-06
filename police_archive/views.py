from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from police_archive.models import Officer, Incident, Details

from police_archive.forms import SearchForm, ComplaintSearchForm

def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

      # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        complaint_form = ComplaintSearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        complaint_form = ComplaintSearchForm()

    return render(request, 'police_archive/search.html', {'form': form, 'complaint_form': complaint_form})

def results(request):
	text = request.GET.get('text', 'default')
	department = request.GET.get('department', 'default')

	try:
		int(text)
		badge=text
	except:
		badge=999999999999   #if text is not a number, make badge number irrelevant


	search_results=Officer.objects.all().filter(
    Q(first_name__icontains=text) | Q(last_name__icontains=text) | Q(badge=badge), Q(department__icontains=department)
)

	return render(request, 'police_archive/results.html', {'text':text,'department':department, 'search_results':search_results})

def complaint_results(request):
	input = request.GET.get('input', 'default')
	search_results=Incident.objects.all().filter(case_number=input)
	return render(request, 'police_archive/complaint_results.html', {'search_results':search_results})

def officer(request, officer_badge):
	officer = Officer.objects.all().get(badge=officer_badge)
	details_list= officer.details_set.all()
	incident_list=[]
	for details in details_list :
		incident_list.append(details.incident)

	return render(request, 'police_archive/officer.html', {'officer':officer,'details_list':details_list, "incident_list":incident_list})

def incident(request, incident_id):
	incident=Incident.objects.all().get(case_number=incident_id)
	officer_list = incident.officers2.all()
	details_list = Details.objects.filter(incident=incident)      
	return render(request, 'police_archive/incident.html', {'incident':incident, 'officer_list':officer_list, 'details_list':details_list})
