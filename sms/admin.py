from django.contrib import admin
from sms.models import *
admin.site.register(SMS)
admin.site.register(Contact)
admin.site.register(Country)
admin.site.register(Route)
admin.site.register(Operator)