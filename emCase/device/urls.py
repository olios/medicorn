from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<id_number>\d+)$', views.view_device, name='index'),
    url(r'^$', views.index, name='index'),    
]
