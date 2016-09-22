from django.shortcuts import render, redirect
from .models import User
from ..belt_reviewer.models import Review
from django.core.urlresolvers import reverse
import bcrypt

def index(request):
	try:
		request.session['message']
	except:
		request.session['message'] = ''
	return render(request, 'login_registration/index.html')

def register(request):
	email_validate = User.objects.validate(request.POST['email'])
	info_validate = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['password'], request.POST['confirm']) 
	password = request.POST['password']
	if email_validate and info_validate:
		request.session['first_name'] = request.POST['first_name']
		request.session['regorlogin'] = 'registered'
		password = password.encode('utf-8')
		hashed = bcrypt.hashpw(password, bcrypt.gensalt())
		first_name = request.POST['first_name'];
		last_name = request.POST['last_name'];
		email = request.POST['email'];
		User.objects.create(email = email, first_name = first_name, last_name = last_name, password = hashed)
		request.session['id'] = User.objects.get(email=request.POST['email']).id
		return redirect(reverse('belt:books_home'))
	elif not email_validate:
		request.session['message'] = "Email is not valid"
	elif not info_validate:
		request.session['message'] = "First Name required and must letters\r\n Last Name required and must have letters \r\n Password Required with no fewer than 8 characters and must match passwowrd confirmation"
	return redirect(reverse('logreg:my_index'))

def login(request):
	login_validate = User.objects.login_valid(request.POST['email'], request.POST['password'])
	if login_validate:
		request.session['message'] = ''
		request.session['id'] = User.objects.get(email=request.POST['email']).id
		request.session['regorlogin'] = 'logged in!'
		return redirect(reverse('belt:books_home'))
	elif not login_validate:
		request.session['message']= 'Wrong login credentials'
	return redirect(reverse('logreg:my_index'))

def home(request):
	return redirect(reverse('belt:books_home'))
def reviewer(request, id):
	context = {
		'reviews': Review.objects.filter(user__id =id),
		'user': User.objects.get(id = id)
	}
	return render(request, 'belt_reviewer/user.html', context)
def logout(request):
	request.session.pop('id')
	return redirect(reverse('logreg:my_index'))