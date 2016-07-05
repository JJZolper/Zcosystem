from django.contrib import admin

from users.models import *

admin.site.register(UserProfile)
admin.site.register(UserEvent)
admin.site.register(City)
admin.site.register(Country)

