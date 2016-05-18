from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.search, name='index'),
    url(r'^officer/(?P<officer_badge>\d+)/', views.officer, name='officer'),
    url(r'^incident/(?P<case_number>\w+\-\w+)/', views.incident, name='incident'),
    

]