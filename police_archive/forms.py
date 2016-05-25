from django import forms
from police_archive.models import Officer

class SearchForm(forms.Form):
    text = forms.CharField(label='Name or Badge Number', max_length=100)
    department_list=Officer.objects.all().values_list('department', flat='true').distinct()
    choices=[('','')]
    for item in department_list :
    	choices.append((item,item))
    department=forms.ChoiceField(choices, label='Department')

class ComplaintSearchForm(forms.Form):
	input = forms.CharField(label='Case Number', max_length=100)