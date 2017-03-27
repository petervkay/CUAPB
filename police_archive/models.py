from __future__ import unicode_literals

from django.db import models
from tinymce import models as tinymce_models





class Officer(models.Model):
	first_name = models.CharField(max_length=80, blank=True, null=True)
	last_name = models.CharField(max_length=80, blank=True, null=True)
	badge = models.IntegerField(blank=True, null=True)
	department = models.CharField(max_length=50, blank=True, null=True)
	model_pic = models.ImageField(upload_to = "police_archive/officer_photos", default= 'noimage', blank=True, null=True)
	description = tinymce_models.HTMLField(blank=True, null=True)

	def __str__(self):
		return self.last_name + ', ' + self.first_name

	class Meta():
		ordering = ['last_name']	

	 



class Incident(models.Model):
	officer = models.ManyToManyField(Officer, through='Details')
	case_number = models.CharField(max_length=50, blank=True)
	department = models.CharField(max_length=50, blank=True, null=True)

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

	class Meta():
		ordering = ['-case_number']

class Details(models.Model):
	officer = models.ForeignKey(Officer, on_delete=models.CASCADE, blank=True)
	incident = models.ForeignKey(Incident, on_delete=models.CASCADE, blank=True)
	allegation = models.CharField(max_length=50, blank=True)
	finding = models.CharField(max_length=50, blank=True)
	action = models.CharField(max_length=50, blank=True)


	def __str__(self):
			return self.officer.first_name + ' '+ self.officer.last_name+ ', ' + self.incident.case_number

	class Meta():
		verbose_name_plural = "details"
		ordering = ['incident__case_number']


class SiteText(models.Model):
	content1 = tinymce_models.HTMLField()
	content2 = models.TextField(max_length=500, blank=True)