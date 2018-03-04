from django.contrib import admin

# Register your models here.
from .models import  Note,  Priority, Status, Task

admin.site.register( ( Note,  Priority, Status, Task ))
