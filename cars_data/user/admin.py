from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Model)
admin.site.register(Auto)
admin.site.register(AutoImage)
admin.site.register(Bewertung)
admin.site.register(AutoZubehor)
admin.site.register(AutoReifen)
admin.site.register(AutoLackMessung)
