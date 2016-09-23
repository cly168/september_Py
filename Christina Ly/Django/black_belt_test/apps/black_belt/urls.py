from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^add$', views.add, name = 'my_add'),
    url(r'^new$', views.new_info, name = 'my_new_info'),

]
