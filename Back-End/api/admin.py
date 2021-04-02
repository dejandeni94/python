from django.contrib import admin
from .models import Users
from .models import Projects
from .models import FileUpload
# Register your models here.

admin.site.register(Users)
admin.site.register(Projects)
admin.site.register(FileUpload)
