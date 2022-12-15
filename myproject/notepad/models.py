from django.db import models
from django.contrib.auth.models import User

#these are for keeping log of succesful and failed login attempts
'''
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver
'''


class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)


#this is an example model for storing succesful and failed login attempts
#this model could be utilized for example in creating fuzzing protection
'''
class AuditEntry(models.Model):
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    username = models.CharField(max_length=256, null=True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)

@receiver(user_logged_in)
def user_logged_in_callback(request, user):  
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_in', ip=ip, username=user)

@receiver(user_login_failed)
def user_login_failed_callback(request, user):
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_login_failed', ip=ip, username=user)
'''
