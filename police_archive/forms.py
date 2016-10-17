from django import forms
from police_archive.models import Officer, Incident
from django.contrib.admin.widgets import FilteredSelectMultiple

class SearchForm(forms.Form):
	text = forms.CharField(label='Name or Badge Number', max_length=100)
	department_list=Officer.objects.all().values_list('department', flat='true').distinct()
	for value in department_list:
		if Officer.objects.all().filter(department=value)==0:
			department_list.remove(value)
	
	choices=[('','')]
	for item in department_list :
		choices.append((item,item))
	department=forms.ChoiceField(choices, label='Department', required=False)

class ComplaintSearchForm(forms.Form):
	input = forms.CharField(label='Case Number', max_length=100)

class IncidentAdminForm(forms.ModelForm):
	class Meta:
		model = Incident
		fields='__all__'

	list_display = ('office','case_number')
	search_fields = ['case_number']
	

	officers = forms.ModelMultipleChoiceField(
		queryset=Officer.objects.all(),
		required=False,
		widget=FilteredSelectMultiple(
			verbose_name='Officers',
			is_stacked=False
		)
	)

	#def __init__(self, *args, **kwargs):
	#	super(IncidentAdminForm, self).__init__(*args, **kwargs)
	#	if self.instance.pk:
	#		self.fields['details'].initial = self.instance.officers_set.all()

	# def save(self, commit=True):
	# 	incident = super(IncidentAdminForm, self).save(commit=False)  
	# 	if commit:
	# 		incident.save()\

	# 	if incident.pk:
	# 		incident_details= Details.objects.get(incident=incident, )
	# 		incident_details.officer = self.cleaned_data['officers']
	# 		self.save_m2m()
	# 	return incident