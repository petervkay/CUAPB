from police_archive.models import Officer, Incident, Details
from django.core.exceptions import ObjectDoesNotExist




def run():
	f = open('C:/Users/peter/websites/CUAPB/police_archive/scripts/complaints.csv', 'r').read()
	input=eval(f)
	print input[1938]




# for row in dataReader:
# if row[0] != 'ZIPCODE': # Ignore the header row, import everything else
# zipcode = ZipCode()
# zipcode.zipcode = row[0]
# zipcode.city = row[1]
# zipcode.statecode = row[2]
# zipcode.statename = row[3]
# zipcode.save()