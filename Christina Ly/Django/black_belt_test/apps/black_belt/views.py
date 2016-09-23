from django.shortcuts import render, redirect
from ..login_registration.models import User
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
	request.session['login_message'] = ""
	request.session['register_message'] = ""
	return render(request, 'user_dashboard/index.html')