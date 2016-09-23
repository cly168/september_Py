from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^dashboard/admin$', views.admin, name='my_admin'),
    url(r'^dashboard$', views.dashboard, name='my_dashboard'),
    url(r'^logout$', views.logout, name ='logout'),
    url(r'^users/show/(?P<id>\d+)$', views.wall, name ='my_wall'),
    url(r'^message/(?P<id>\d+)$', views.post_message, name ="post_message"),
    url(r'^comment/(?P<id>\d+)$', views.post_comment, name="post_comment")
]