from django import forms
from police_archive.models import Officer, SiteText
from tinymce.widgets import TinyMCE

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


class AdminTextForm(forms.ModelForm):

    content1 = forms.CharField(widget=TinyMCE(attrs={'cols': 10, 'rows': 30}))
    content2= forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 30}))

    class Meta:
        model = SiteText
        fields= '__all__'

class OfficerTextForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 30}))

    class Meta:
        model = SiteText
        fields= '__all__'