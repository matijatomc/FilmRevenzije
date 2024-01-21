from django.contrib import admin
from .models import *

model_list = [Film, Recenzija]
admin.site.register(model_list)