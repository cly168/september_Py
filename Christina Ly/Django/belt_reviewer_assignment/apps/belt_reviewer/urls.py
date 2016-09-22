from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name= 'books_home'),
    url(r'^add$', views.add, name= 'add'),
    url(r'^create$', views.create, name= 'create'),
    url(r'^(?P<id>\d+)$', views.detail, name ="detail"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name= 'delete'),
    url(r'^update/(?P<id>\d+)$', views.update, name ='update'),
]
