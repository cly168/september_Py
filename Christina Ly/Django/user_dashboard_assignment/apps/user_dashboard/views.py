from django.shortcuts import render, redirect
from ..login_registration.models import User, Message, Comment
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
def wall(request, id):
	messages = Message.objects.filter(user_id = id)
	context = {
		'user': User.objects.get(id=id),
		'messages':messages
	}
	# 'messages':Message.objects.filter(user_id = id),
	return render(request, 'user_dashboard/wall.html', context)
def post_message(request, id):
	user = User.objects.get(id=id)
	messenger=User.objects.get(id=request.session['id'])
	message = request.POST['message']
	message= Message.objects.create(message=message, user = user, messenger=messenger)
	return redirect(reverse('user_dashboard:my_wall', kwargs={'id':id}))
def post_comment(request,id):
	user= User.objects.get(id = request.session['id'])
	comment=request.POST['comment']
	message = Message.objects.get(id=id)
	comment=Comment.objects.create(user=user, message = message, comment=comment)
	return redirect(reverse('user_dashboard:my_wall', kwargs={'id':message.user.id}))