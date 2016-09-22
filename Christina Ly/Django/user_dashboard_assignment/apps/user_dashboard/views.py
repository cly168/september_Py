from django.shortcuts import render, redirect
from ..login_registration.models import User
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
	request.session['login_message'] = ""
	request.session['register_message'] = ""
	return render(request, 'user_dashboard/index.html')
def admin(request):
	context={
		'users': User.objects.all()
	}
	return render(request, 'user_dashboard/admin.html', context)
def dashboard(request):
	context={
		'users': User.objects.all()
	}
	if User.objects.get(id = request.session['id']).user_level ==9: ##if admin(9), then go to admin.html
		return redirect(reverse('user_dashboard:my_admin'))
	return render(request, 'user_dashboard/dashboard.html', context) ##else go to dashboard
def logout(request):
	request.session.pop('id')
	return redirect(reverse('user_dashboard:my_index'))	