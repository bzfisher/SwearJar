from django.db import models

# Create your models here.
class User(models.Model):
	people = models.Manager();
	swearCount = models.PositiveSmallIntegerField(default=0)
	phoneNumber = models.CharField(max_length=12, unique=False)
	momsNumber = models.CharField(max_length=12)
	userName = models.CharField(max_length=128)
	lastChecked = models.DateTimeField(auto_now=True)
	stripeAccount = models.CharField(max_length=25600, unique=False)
	swears = models.CharField(max_length=25600)
	password = models.CharField(max_length=200)
	###error check if unique is screwed up
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.userName
