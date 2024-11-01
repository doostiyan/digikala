from django.contrib import admin
from django.contrib.auth.models import User

from accounts.models import Profile

# Register your models here.
admin.site.register(Profile)

class ProfileInline(admin.StackedInline):
    model = Profile

class ProfileAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    model = User
    fields = ['username', 'last_name', 'first_name', 'email']

admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)