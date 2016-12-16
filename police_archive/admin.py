from django.contrib import admin
from import_export import resources, widgets, fields
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from forms import AdminTextForm, OfficerTextForm

from .models import Officer, Incident, Details, SiteText

class DetailsInlineAdmin (admin.TabularInline):
	model = Details
	extra = 5
	



class OfficerResource(resources.ModelResource):

	class Meta:
		model = Officer
		
class OfficerAdmin(ImportExportModelAdmin):
	list_display = ('first_name', 'last_name', 'badge', 'department')
	search_fields = ['first_name', 'last_name']
	inlines = [DetailsInlineAdmin]
	resource_class = OfficerResource

	form=OfficerTextForm

	class Media:
		js = ('//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js','/static/admin/js/admin/popup.js')



class IncidentResource(resources.ModelResource):


	class Meta:
		fields = ('officer','case_number', 'office')
		model = Incident
		import_id_fields = ['case_number']

class IncidentAdmin(ImportExportModelAdmin):
	list_display = ('office','case_number')
	search_fields = ['case_number']
	inlines = [DetailsInlineAdmin]
	resource_class = IncidentResource




class DetailsResource(resources.ModelResource):

	class BadgeForeignKeyWidget(widgets.ForeignKeyWidget):
	    def get_queryset(self, value, row):
	        return self.model.objects.filter(
	            badge__iexact=row["badge"]
	        )

	officer = fields.Field(
		column_name='officer',
		attribute='officer',
		widget=BadgeForeignKeyWidget(Officer, 'last_name'))

	incident = fields.Field(
		column_name='incident',
		attribute='incident',
		widget=widgets.ForeignKeyWidget(Incident, 'case_number'))

	class Meta:
		fields = ('id','officer','incident', 'allegation', 'finding', 'action')
		model = Details
		

class DetailsAdmin(ImportExportModelAdmin):
	list_display=('incident','officer', 'allegation', 'finding', 'action')
	search_fields = ['officer__last_name', 'incident__case_number']
	resource_class = DetailsResource

class SiteTextAdmin(admin.ModelAdmin):
	form=AdminTextForm





admin.site.register(Officer, OfficerAdmin)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(Details, DetailsAdmin)
admin.site.register(SiteText, SiteTextAdmin)