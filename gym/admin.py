from django.contrib import admin

from .models import Member,Contact,Services,UserProfile



admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(Services)
admin.site.register(UserProfile)