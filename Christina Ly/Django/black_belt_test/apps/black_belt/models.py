from __future__ import unicode_literals
from django.db import models
from ..login_registration.models import User
from datetime import datetime
import re
class TravelManager(models.Manager):
	def date_valid(self, start, end):
		now = datetime.now()
		start = datetime.strptime(start, "%Y-%m-%d") 
		end = datetime.strptime(end, "%Y-%m-%d")
		if start < now:
			return False
		if end < now or end < start:
			return False
		return True
	def trip_name(self, plan, destination):
		NAME_REGEX = re.compile(r'^[a-zA-Z-]{2,}$')
		if not NAME_REGEX.match(destination):
			return False
		elif not NAME_REGEX.match(plan):
			return False
		return True
class Travel(models.Model):
	user = models.ForeignKey(User)
	destination = models.CharField(max_length = 255)
	start = models.DateField()
	end = models.DateField()
	plan = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = TravelManager()

class Guest(models.Model):
	travel = models.ForeignKey(Travel)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)