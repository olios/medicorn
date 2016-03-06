from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^visual$', views.visualization, name='visualization'),
    url(r'^view_device/(?P<id_number>\d+)$', views.view_device, name='view_device'),
    url(r'^$', views.index, name='index'),    
]
