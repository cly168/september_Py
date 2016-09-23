from __future__ import unicode_literals
from django.db import models
from ..login_registration.models import User

class Travel(models.Model):
	user = models.ForeignKey(User)
	destination = models.CharField(max_length = 255)
	start = models.DateField()
	end = models.DateField()
	plan = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
