from django.contrib import admin

from .models import Officer, Incident, Details

class DetailsInlineAdmin (admin.TabularInline):
	model = Details
	extra = 5

class OfficerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'badge', 'department')
    search_fields = ['first_name', 'last_name']
    inlines = [DetailsInlineAdmin]

class IncidentAdmin(admin.ModelAdmin):
	list_display = ('office','case_number')
	search_fields = ['case_number']
	inlines = [DetailsInlineAdmin]

class DetailsAdmin(admin.ModelAdmin):
	list_display=('incident','officer', 'allegation', 'finding', 'action')
	search_fields = ['officer__last_name', 'incident__case_number']



admin.site.register(Officer, OfficerAdmin)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(Details, DetailsAdmin)