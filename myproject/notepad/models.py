from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

'''class Note(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    input_text = models.CharField(max_length=200)'''