from django.shortcuts import render, redirect
from ..login_registration.models import User
from .models import Travel
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
	request.session['login_message'] = ""
	request.session['register_message'] = ""
	id = request.session['id']
	context={
		'user': User.objects.get(id=id),
		'my_travels':Travel.objects.filter(user_id=id),
		'other_travels':Travel.objects.exclude(user_id=id)
	}
	return render(request, 'black_belt/index.html', context)
def add(request):
	id = request.session['id']
	context={
		'user': User.objects.get(id=id),
		'my_travels':Travel.objects.filter(user_id=id),
	}
	return render(request, 'black_belt/add.html', context)
def new_info(request):
	user = User.objects.get(id =request.session['id'])
	travel=Travel.objects.create(user = user, destination = request.POST['destination'], plan = request.POST['plan'], start = request.POST['start'], end = request.POST['end'])	
	return redirect(reverse('black_belt:my_index'))
def destination(request, id):
	context={
		'travel': Travel.objects.get(id=id)
	}
	return render(request, 'black_belt/destination.html', context)
def join(request, id):
	user = User.objects.get(id =request.session['id'])
	travel=Travel.objects.create(destination= destination.id, )
	return redirect(reverse('black_belt:my_destination', kwargs={'id':id}))