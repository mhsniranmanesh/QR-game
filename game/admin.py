from django.contrib import admin

# Register your models here.
from game.models import Slogan, Submit, Barcode

admin.site.register(Barcode)
admin.site.register(Submit)
admin.site.register(Slogan)