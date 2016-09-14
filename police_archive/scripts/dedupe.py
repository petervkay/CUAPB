from __future__ import unicode_literals
from police_archive.models import Incident, Details, Officer
from django.db.models import Count



def run() :

	#get list of duplicates
	list=Incident.objects.values('case_number').annotate(case_number_count=Count('case_number')).exclude(case_number_count=1)
	g= []
	
	#make list of case numbers
	for item in list:
		g.append(item['case_number'])
	
		

	#first entry was empty, remove first entry
	for number in g[:1:] :
		
	#get list of incident objets
		old_incidents=Incident.objects.filter(case_number=number);
		print old_incidents
		
		#make new object to replace old ones
		new_incident = Incident(case_number=number)
		new_incident.office=old_incidents[0].office

		#filter out all details which match one of the incidents
		details_list=Details.objects.none()
		for incident in old_incidents:
			results=Details.objects.filter(incident=incident)
			details_list = details_list | results

		#delete old_incidents so that details can be modified
		
		new_incident.save()
		
		#create new details objects pointing to new incident object, delete old details object
		for details in details_list:
			
			new_details = Details.objects.create(incident=new_incident,officer=details.officer, allegation=details.allegation, finding=details.finding, action=details.action)
			new_details.save()
			details.delete()
		

		#delete old incidents not new_incident
		junk = old_incidents.exclude(pk=new_incident.pk)
		print junk
		junk.delete()
		



		

		
	
		
		






		