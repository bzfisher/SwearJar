from django.db import models

# Create your models here.
class User(models.Model):
  swearCount = models.PositiveSmallIntegerField(default=0)
  phoneNumber = models.CharField(max_length=12, unique=True)
  momsNumber = models.CharField(max_length=12)
  userName = models.CharField(max_length=128)
  lastChecked = models.DateTimeField()
  ###stripeAccount = models.CharField(max_length=256, unique=True)
  swears = models.CharField(max_length=25600)
  password = models.CharField(max_length=200)
  ###error check if unique is screwed up
