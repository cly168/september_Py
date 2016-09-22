from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
	request.session['register_message'] = ""
	try:
		request.session['login_message']
	except:
		request.session['login_message'] = ''
	try:
		request.session['id']
		return redirect(reverse('user_dashboard:my_dashboard'))#######
	except:
		return render(request, 'login_registration/index.html')
def reg(request):
	request.session['login_message'] = ""
	try:
		request.session['register_message']
	except:
		request.session['register_message'] = ''
	return render(request, 'login_registration/register.html')
def register(request):
	email_validate = User.objects.validate(request.POST['email'])
	info_validate = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['password'], request.POST['confirm']) 
	password = request.POST['password']
	if email_validate and info_validate:
		request.session['register_message'] = " "
		request.session['first_name'] = request.POST['first_name']
		request.session['regorlogin'] = 'registered'
		password = password.encode('utf-8')
		hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		count = User.objects.all().count()
		if count == 0:
			user_level = 9
		else:
			user_level = 0
		User.objects.create(email = email, first_name = first_name, last_name = last_name, password = hashed, user_level = user_level)
		request.session['id'] = User.objects.get(email =request.POST['email']).id
		return redirect(reverse('user_dashboard:my_dashboard'))
	elif not email_validate:
		request.session['register_message'] = "Email is not valid"
	elif not info_validate:
		request.session['register_message'] = "First Name required and must letters\r\n Last Name required and must have letters \r\n Password Required with no fewer than 8 characters and must match password confirmation"
	return redirect(reverse('logreg:my_reg'))
def login(request):
	login_validate = User.objects.login_valid(request.POST['email'], request.POST['password'])
	if login_validate:
		request.session['id'] = User.objects.get(email =request.POST['email']).id
		request.session['login_message'] = ''
		request.session['first_name'] = User.objects.get(email =request.POST['email']).first_name
		request.session['regorlogin'] = 'logged in!'
		return redirect(reverse('user_dashboard:my_dashboard'))
	elif not login_validate:
		request.session['login_message']= 'Wrong login credentials'
		return redirect(reverse('logreg:my_index'))
def create(request):
	request.session['login_message'] = ""
	try:
		request.session['register_message']
	except:
		request.session['register_message'] = ''
	return render(request, 'login_registration/create.html')
def validate_create(request):
	email_validate = User.objects.validate(request.POST['email'])
	info_validate = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['password'], request.POST['confirm']) 
	password = request.POST['password']
	if email_validate and info_validate:
		request.session['register_message'] = " "
		request.session['first_name'] = request.POST['first_name']
		request.session['regorlogin'] = 'registered'
		password = password.encode('utf-8')
		hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		count = User.objects.all().count()
		if count == 0:
			user_level = 9
		else:
			user_level = 0
		User.objects.create(email = email, first_name = first_name, last_name = last_name, password = hashed, user_level = user_level)
		return redirect(reverse('user_dashboard:my_admin'))
	elif not email_validate:
		request.session['register_message'] = "Email is not valid"
	elif not info_validate:
		request.session['register_message'] = "First Name required and must letters\r\n Last Name required and must have letters \r\n Password Required with no fewer than 8 characters and must match password confirmation"
	return redirect(reverse('logreg:my_create'))
def remove_user(request, id):
	User.objects.get(id=id).delete()
	return redirect(reverse('user_dashboard:my_admin')) 

def validate_edit(request, id):
	email_validate = User.objects.validate(request.POST['email'])
	info_validate = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['password'], request.POST['confirm']) 
	password = request.POST['password']
	if email_validate and info_validate:
		request.session['register_message'] = " "
		password = password.encode('utf-8')
		hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		User.objects.create(email = request.POST['email'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], user_level = user_level)
		return redirect(reverse('user_dashboard:my_admin', kwargs={'id':id}))
	elif not email_validate:
		request.session['register_message'] = "Email is not valid"
	elif not info_validate:
		request.session['register_message'] = "First Name required and must letters\r\n Last Name required and must have letters \r\n Password Required with no fewer than 8 characters and must match password confirmation"
	return redirect(reverse('logreg:edit_admin'))

def edit_admin(request, id):
	context = {
		"user": User.objects.get(id = id)
	}
	return render(request, 'login_registration/edit.html', context)

def update_admin(request, id):
	return render('user_dashboard/admin.html')