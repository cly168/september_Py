from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
	def validate(self, email):
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if not EMAIL_REGEX.match(email):
			return False
		else:
			return True
			
	def login_valid(self, email, password):
		try:
			user = User.objects.get(email = email)
			if user:
				password = password.encode()
				if bcrypt.hashpw(password, user.password.encode()) ==  user.password.encode():
					return True
				else:
					return False
		except:			
			return False

	def register(self, first_name, last_name, password, confirm):
		NAME_REGEX = re.compile(r'^[a-zA-Z-]{2,}$')
		PASSWORD_REGEX = re.compile(r'^.{8,}$')
		if not NAME_REGEX.match(first_name):
			return False
		elif not NAME_REGEX.match(last_name):
			return False
		elif not PASSWORD_REGEX.match(password):
			return False
		elif  not password == confirm:
			return False
		else:		
			return True
class User(models.Model):
	first_name = models.CharField(max_length = 45)
	last_name = models.CharField(max_length = 45)
	email = models.CharField(max_length = 45)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

