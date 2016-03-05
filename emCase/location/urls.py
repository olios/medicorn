from django.conf.urls import url
from . import views


urlpatterns = [
	#url(r'^view_device/(?P<id_number>\d+)$', views.view_device, name='view_device'),
    url(r'^run_loc$', views.run_location, name='run_location'),    
    url(r'^$', views.index_location, name='index'),    
]
