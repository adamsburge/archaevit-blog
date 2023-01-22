from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser

# Register your models here.
fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'institution', 'role')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(NewUser, UserAdmin)
