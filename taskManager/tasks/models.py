from django.db import models
from django.utils import timezone

# Create your models here.
class Priority( models.Model ):
    label = models.CharField(max_length=20, unique=True)
    value = models.IntegerField(unique=True)


class Status( models.Model ):
    label = models.CharField(max_length=20, unique=True)
    value = models.IntegerField(unique=True)


class Task( models.Model ):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=8000)
    fk_parent = models.ForeignKey('self', on_delete=models.CASCADE)
    fk_priority = models.ForeignKey(Priority, on_delete=models.PROTECT )
    fk_status = models.ForeignKey(Status, on_delete=models.PROTECT)
    creation_date = models.DateField(default = timezone.now) # creation date for the task record
    ending_date = models.DateField(default = timezone.now) # Planned closing date for the task
    closing_date = models.DateField(default = timezone.now) # closing date for the task
    modification_date = models.DateField(default = timezone.now) # last modification date
    # Tag management later
    # Assegnazione task later


class Note( models.Model ):
    note = models.CharField(max_length=800)
    creation_date = models.DateField(default = timezone.now)
    fk_task = models.ForeignKey( Task, on_delete=models.CASCADE )

    
