from django.contrib import admin

# Register your models here.

from polling.models import Poll

admin.site.register(Poll)
