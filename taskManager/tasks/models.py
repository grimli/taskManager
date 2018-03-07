from django.db import models
from django.utils import timezone

# Create your models here.
class Priority( models.Model ):
    label = models.CharField(max_length=20, unique=True)
    value = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.label


class Status( models.Model ):
    label = models.CharField(max_length=20, unique=True)
    value = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.label


class Task( models.Model ):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=8000)
    fk_parent = models.ForeignKey('self', on_delete=models.CASCADE,
            blank=True, null=True, default=None )
    fk_priority = models.ForeignKey(Priority, on_delete=models.PROTECT,
            blank=True, null=True, default=None )
    fk_status = models.ForeignKey(Status, on_delete=models.PROTECT,
            blank=True, null=True, default=None)
    creation_date = models.DateField(default = timezone.now)
            # creation date for the task record
    ending_date = models.DateField( null=True, blank=True,
            default=None) # Planned closing date for the task
    closing_date = models.DateField( null=True, blank=True,
            default=None) # closing date for the task
    modification_date = models.DateField(default = timezone.now)
            # last modification date
    # Tag management later
    # Assegnazione task later
    
    def __str__(self):
        return self.name


class Note( models.Model ):
    note = models.CharField(max_length=800)
    creation_date = models.DateField(default = timezone.now)
    fk_task = models.ForeignKey( Task, on_delete=models.CASCADE )

    
