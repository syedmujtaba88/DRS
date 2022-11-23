from django.contrib import admin
from webapp.models import NumberSync, DeviceSync, FixedNumberSync, Jobs

# Register your models here.
admin.site.register(NumberSync)
admin.site.register(DeviceSync)
admin.site.register(FixedNumberSync)
admin.site.register(Jobs)
