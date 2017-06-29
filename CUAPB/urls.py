"""CUAPB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin


from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.conf import settings
from django.conf.urls.static import static

from police_archive import views





urlpatterns = [
    url(r'^admin/backup/', views.backup),
    url(r'^$', lambda r: HttpResponseRedirect('police_archive/')),
	url(r'^police_archive/', include('police_archive.urls')),
	url(r'^admin/', admin.site.urls),
	url(r'^tinymce/', include('tinymce.urls')),
  
  
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)