from django.shortcuts import render, redirect
from ..login_registration.models import User
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
	try:
		request.session['message']
	except:
		request.session['message'] = ''
	return render(request, 'login_registration/index.html')
def register(request):
	info_validate = User.objects.register(request.POST['first_name'],request.POST['username'],request.POST['password'], request.POST['confirm']) 
	password = request.POST['password']
	if info_validate:
		request.session['message'] = " "
		request.session['first_name'] = request.POST['first_name']
		password = password.encode('utf-8')
		hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		first_name = request.POST['first_name']
		username = request.POST['username']
		User.objects.create(first_name = first_name, username = username, password = hashed)
		request.session['id'] = User.objects.get(username=request.POST['username']).id
		return redirect(reverse('black_belt:my_index'))
	elif not info_validate:
		request.session['message'] = "First Name required and must letters\r\n Username required and must have letters \r\n Password Required with no fewer than 8 characters and must match passwowrd confirmation"
		return redirect(reverse('logreg:my_index'))
def login(request):
	login_validate = User.objects.login_valid(request.POST['username'], request.POST['password'])
	if login_validate:
		request.session['message'] = ''
		request.session['id'] = User.objects.get(username=request.POST['username']).id
		request.session['first_name'] = User.objects.get(username =request.POST['username']).first_name
		return redirect(reverse('black_belt:my_index'))
	elif not login_validate:
		request.session['message']= 'Wrong login credentials'
	return redirect(reverse('logreg:my_index'))
def success(request):
	return render(request, 'black_belt/index.html')
def logout(request):
	request.session.pop('id')
	return redirect(reverse('logreg:my_index'))