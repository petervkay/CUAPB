from __future__ import unicode_literals

from django.db import models




class Officer(models.Model):
    first_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=80, blank=True)
    badge = models.IntegerField(blank=True)
    department = models.CharField(max_length=50, blank=True)

    def __str__(self):
    	return self.last_name + ', ' + self.first_name

     



class Incident(models.Model):
	officers2 = models.ManyToManyField(Officer, through='Details')
	case_number = models.CharField(max_length=50, blank=True)

	OFFICE_CHOICES = (
    ('CRA', 'Civilian Review Authority'),
    ('IA', 'Internal Affairs'),
    ('OPCR', 'Office of Police Conduct Review'),
	)
	office = models.CharField(max_length=10,
	choices=OFFICE_CHOICES,
	)

	def __str__(self):
		return self.case_number

class Details(models.Model):
	officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
	incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
	allegation = models.CharField(max_length=50, blank=True)
	finding = models.CharField(max_length=50, blank=True)
	action = models.CharField(max_length=50, blank=True)


	def __str__(self):
		return unicode(self.officer.first_name) + ' '+ unicode(self.officer.last_name)+ ', ' + unicode(self.incident)

	class Meta():
		verbose_name_plural = "details"
