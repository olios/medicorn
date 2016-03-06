from django.conf.urls import url
from . import views


urlpatterns = [
	#url(r'^view_device/(?P<id_number>\d+)$', views.view_device, name='view_device'),
    url(r'^location$', views.view_location, name='location'),    
    url(r'^stop$', views.stop, name='stop'),    
    url(r'^$', views.run_location, name='index'),    
    url(r'^view_locations$', views.view_location, name='view_location'),
]
