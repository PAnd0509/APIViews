from django.db import models

#Imports from other apps
from apps.users.models import User

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=60, null=False,blank=False)
    init_date=models.DateTimeField()
    end_date=models.DateTimeField()

    def __str__(self)->str:
        return self.name

class Task(models.Model):
    description=models.CharField(max_length=250)
    end_date=models.DateTimeField()
    project=models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    ALTA = "A"
    PEPE = "P"
    BAJA = "B"
    TASK_TYPE_CHOICES = {
        ALTA : "Alta",
        PEPE : "Pp",
        BAJA : "Baja"
    }
    task_type = models.CharField(
        max_length=13,
        choices=TASK_TYPE_CHOICES,
        default=PEPE
    )

class Comment(models.Model):
    init_date=models.DateTimeField()
    content=models.CharField(max_length=120)
    task=models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)