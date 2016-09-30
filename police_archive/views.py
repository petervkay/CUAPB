from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from police_archive.models import Officer, Incident, Details, SiteText
from string import ascii_uppercase
from django.template import RequestContext
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

    text = SiteText.objects.get(id=1)

    return render(request, 'police_archive/search.html', {
        'SiteText':text, 'form': form, 'complaint_form': complaint_form, 'alphabet':ascii_uppercase, 'class_name':'home'})

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
	search_results = search_results.order_by('last_name')
	return render(request, 'police_archive/results.html', {
        'text':text,'department':department, 'search_results':search_results, 'class_name':'results'})

def complaint_results(request):
	input = request.GET.get('input', 'default')
	search_results=Incident.objects.all().filter(case_number=input)
	return render(request, 'police_archive/complaint_results.html', {
        'search_results':search_results, 'class_name':'complaint_results'})

def officer(request, officer_id):
	officer_id = int(officer_id)
	officer = Officer.objects.get(id=officer_id)
	details_list= officer.details_set.all()
	incident_list=[]
	for details in details_list :
		incident_list.append(details.incident)

	return render(request, 'police_archive/officer.html', {
        'officer':officer,'details_list':details_list, "incident_list":incident_list, 'class_name':'officer'})

def incident(request, incident_id):
	incident=Incident.objects.all().get(case_number=incident_id)
	officer_list = incident.officers2.all()
	officer_list = officer_list.order_by('last_name')
	details_list = Details.objects.filter(incident=incident)
	return render(request, 'police_archive/incident.html', {
        'incident':incident, 'officer_list':officer_list, 'details_list':details_list, 'class_name':'incident'})

def browse(request, letter):
	officer_list = Officer.objects.filter(last_name__startswith=letter)
	officer_list = officer_list.order_by('last_name')
	return render(request, 'police_archive/browse.html', {
        'officer_list':officer_list,'class_name':'browse', 'alphabet':ascii_uppercase})



