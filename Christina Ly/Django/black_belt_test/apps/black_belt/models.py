from __future__ import unicode_literals
from django.db import models
from ..login_registration.models import User

class Travel(models.Model):
	user = models.ForeignKey(User)
	destination = models.CharField(max_length = 255)
	start = models.CharField(max_length = 20)
	end = models.CharField(max_length = 20)
	plan = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Guest(models.Model):
	travel = models.ForeignKey(Travel)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)