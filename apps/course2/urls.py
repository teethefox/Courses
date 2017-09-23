from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'add$', views.add),
    url(r'create$', views.create),
    url(r'um/(?P<id>\d+)$', views.um),
    url(r'delete/(?P<id>\d+)$', views.delete)


]