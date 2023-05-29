from django.contrib import admin
from .models import Menu, MenuCategories,Logger, Reservation,Registration

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategories)
admin.site.register(Logger)
admin.site.register(Reservation)
admin.site.register(Registration)

