from optparse import AmbiguousOptionError
from django.contrib import admin

# import you models
from .models import Ferret, Feeding, Toy

# Register your models here.
admin.site.register(Ferret)
admin.site.register(Feeding)
admin.site.register(Toy)