from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.search, name='index'),
	# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^results/$', views.results, name='results'),
	url(r'^complaint_results/$', views.complaint_results, name='complaint_results'),
	url(r'^officer/(?P<officer_badge>\d+)/', views.officer, name='officer'),
	url(r'^complaint/(?P<incident_id>\d+)/', views.incident, name='incident'),


    # url(r'^officer/(?P<officer_badge>\d+)/', views.officer, name='officer'),
    # url(r'^incident/(?P<case_number>\w+\-\w+)/', views.incident, name='incident'),


]