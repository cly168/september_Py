from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "my_index"),
    url(r'^reg$', views.reg, name = "my_reg"),
    url(r'^validate_register$', views.register, name = "validate_reg"),
    url(r'^validate_login$', views.login, name = "validate_login"),
    url(r'^success$', views.success, name = "my_success")
]