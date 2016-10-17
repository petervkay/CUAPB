from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

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

    class Media:
    	js = ('//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js','/static/admin/js/admin/popup.js')



    

class IncidentAdmin(admin.ModelAdmin):
	list_display = ('office','case_number')
	search_fields = ['case_number']
	inlines = [DetailsInlineAdmin]

class DetailsAdmin(admin.ModelAdmin):
	list_display=('incident','officer', 'allegation', 'finding', 'action')
	search_fields = ['officer__last_name', 'incident__case_number']

class SiteTextAdmin(admin.ModelAdmin):
	list_display=('content1','content2')





admin.site.register(Officer, OfficerAdmin)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(Details, DetailsAdmin)
admin.site.register(SiteText, SiteTextAdmin)