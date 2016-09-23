from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):	
	def login_valid(self, username, password):
			user = User.objects.get(username = username)
			if user:
				password = password.encode()
				if bcrypt.hashpw(password, user.password.encode()) ==  user.password.encode():
					return True
				else:
					return False
			else:
				return False

	def register(self, first_name, username, password, confirm):
		NAME_REGEX = re.compile(r'^[a-zA-Z-]{3,}$')
		PASSWORD_REGEX = re.compile(r'^.{8,}$')
		if not NAME_REGEX.match(first_name):
			return False
		elif not NAME_REGEX.match(username):
			return False
		elif not PASSWORD_REGEX.match(password):
			return False
		elif  not password == confirm:
			return False
		else:		
			return True

class User(models.Model):
	first_name = models.CharField(max_length = 45)
	username = models.CharField(max_length = 45)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

