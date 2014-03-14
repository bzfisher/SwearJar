from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    phoneNumber = models.CharField(max_length=12)
    momsNumber = models.CharField(max_length=12)
    swears = models.CharField(max_length=25600)
    lastChecked = models.DateTimeField(auto_now=True)
    swearCount = models.PositiveSmallIntegerField(default=0)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username