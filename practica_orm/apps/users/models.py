from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    REQUIRED_FIELDS=["email"]
    
    #email=models.EmailField(unique=True)

    def save(self, *args, **kwargs) -> None:
        self.username=self.email.split("@")[0]
        return super().save(*args, **kwargs)
    
class Member(models.Model):
    user=models.ForeignKey('User',on_delete=models.DO_NOTHING)
    project=models.ForeignKey('projects.Project', on_delete=models.DO_NOTHING)
    rol=models.CharField(max_length=60)
    date=models.DateTimeField()
    DIRECTOR = "Dir"
    GERENTE = "Ger"
    JUNIOR = "Jun"
    SUPERVISOR = "Sup"
    DESARROLLADOR = "Dev"
    MEMBER_TYPE_CHOICES = {
        DIRECTOR :"Director",
        GERENTE : "Gerente",
        JUNIOR : "Junior",
        SUPERVISOR : "Supervisor",
        DESARROLLADOR :"Desarrollador"
    }
    member_type = models.CharField(
        max_length=13,
        choices=MEMBER_TYPE_CHOICES,
        default=DESARROLLADOR,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}
    def __str__(self):
        return f'{self.user.username} - {self.project.name}'
    
    
class Owner(models.Model):
    user=models.ForeignKey('User',on_delete=models.DO_NOTHING)
    task=models.ForeignKey('projects.Task', on_delete=models.DO_NOTHING)