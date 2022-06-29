from django.contrib import admin
from .models import *

admin.site.register(ServerType)
admin.site.register(DiskType)
admin.site.register(Owner)
admin.site.register(Location)
admin.site.register(Server)