from django.shortcuts import render, redirect
from ..login_registration.models import User
from .models import Travel
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
	request.session['login_message'] = ""
	request.session['register_message'] = ""
	context={
		'my_travels':Travel.objects.filter(user.id=request.session['id']),
		'other_travels':Travel.objects.exclude(id=id)
	}
	return render(request, 'black_belt/index.html', context)
def add(request):
	context={
		"travels": Travel.objects.all()
	}
	return render(request, 'black_belt/add.html', context)
def new_info(request):
	user = User.objects.get(id =request.session['id'])
	travel=Travel.objects.create(user = user, destination = request.POST['destination'], plan = request.POST['plan'], start = request.POST['start'], end = request.POST['end'])	
	return redirect(reverse('black_belt:my_index'))
