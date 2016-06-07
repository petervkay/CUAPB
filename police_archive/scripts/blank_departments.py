from police_archive.models import Incident, Details, Officer

def run() :
	o = Officer.objects.filter(department='Minneapolis ')
	for officer in o:
		officer.department='Minneapolis'
		officer.save()