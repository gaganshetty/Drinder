from django.contrib import admin
from regaleapp.models import Person, Cusine, Location, Restaurant

# Register your models here.
my_models = [Person, Cusine, Location, Restaurant]
admin.site.register(my_models)