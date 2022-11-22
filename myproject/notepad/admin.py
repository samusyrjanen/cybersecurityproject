from django.contrib import admin

from .models import Account
from .models import Note

admin.site.register(Account)
admin.site.register(Note)