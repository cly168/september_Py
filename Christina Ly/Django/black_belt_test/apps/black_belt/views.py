from django.shortcuts import render, redirect
from ..login_registration.models import User
from .models import Travel, Guest
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
	request.session['message'] = " "
	request.session['login_message'] = ""
	request.session['register_message'] = ""
	id = request.session['id']
	user = User.objects.get(id=id)
	context={		
		'user': User.objects.get(id=id),
		'my_travels':Guest.objects.filter(user_id=id),
		'other_travels':Travel.objects.exclude(user__id=id).exclude(guest__user_id=user.id),
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
	add_valid = Travel.objects.date_valid(request.POST['start'], request.POST['end'])
	add_valid_info = Travel.objects.trip_name(request.POST['destination'], request.POST['plan'])
	if add_valid and add_valid_info:
		request.session['message'] = " "
		user = User.objects.get(id =request.session['id'])
		travel=Travel.objects.create(user = user, destination = request.POST['destination'], plan = request.POST['plan'], start = request.POST['start'], end = request.POST['end'])	
		guest = Guest.objects.create(travel=travel, user = user)
		return redirect(reverse('black_belt:my_index'))
	elif not add_valid_info:
		request.session['message'] = "Need to input destination and plan"
		return redirect(reverse('black_belt:my_add'))

	else:
		request.session['message'] = "Invalid date choice"
		return redirect(reverse('black_belt:my_add'))

def destination(request, id):
	travel= Travel.objects.get(id=id)
	context={
		'travel': Travel.objects.get(id=id),
		'guests': Guest.objects.filter(travel=travel)
	}
	return render(request, 'black_belt/destination.html', context)
def join(request, id):
	user = User.objects.get(id =request.session['id'])
	travel=Travel.objects.get(id=id)
	guest = Guest.objects.create(travel=travel, user=user)
	user.save()
	return redirect(reverse('black_belt:my_destination', kwargs={'id':id}))

