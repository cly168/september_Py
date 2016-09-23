from django.shortcuts import render, redirect
from ..login_registration.models import User
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
	request.session['login_message'] = ""
	request.session['register_message'] = ""
	context={
		'user':User.objects.get(id=request.session['id']),
		'travels':Travel.objects.all()
	}
	return render(request, 'black_belt/index.html', context)