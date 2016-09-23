from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "my_index"),
    url(r'^reg$', views.reg, name = "my_reg"),
    url(r'^validate_register$', views.register, name = "validate_reg"),
    url(r'^validate_login$', views.login, name = "validate_login"),
    url(r'^users/new$', views.create, name = "my_create"),
    url(r'^users/create_valid$', views.validate_create, name ="validate_create"),
    url(r'^users/remove_user(?P<id>\d+)$', views.remove_user, name = "remove_user"),
    url(r'^users/(?P<id>\d+)$', views.edit_admin, name = "my_edit_admin"),
    url(r'^users/edit_valid/(?P<id>\d+)$', views.validate_edit, name ="validate_edit"),
    url(r'^user/edit/(?P<id>\d+)$', views.update_admin, name = "my_update_admin"),
    url(r'^user/edit/password/(?P<id>\d+)$', views.validate_create_password, name ="validate_create_password"),
    url(r'^user/edit/profile/(?P<id>\d+)$', views.edit_profile, name ="edit_profile"),
    url(r'^user/edit/description/(?P<id>\d+)$', views.description_edit, name ="description_edit")


]