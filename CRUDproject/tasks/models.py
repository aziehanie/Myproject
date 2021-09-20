from django.db import models

# Create your models here.

class Status(models.TextChoices):
    UNSTARTED = 'u', "Area"
    ONGOING = 'o', "Perimeter"
    # FINISHED = 'f', "Finished"


class Task(models.Model):
    name = models.CharField(verbose_name="Shape type", max_length=65, unique=True)
    status = models.CharField(verbose_name="Calculate shape", max_length=1, choices=Status.choices)

    def __str__(self):
        return self.name

# tasks/forms.py
from .models import Task
from django import forms

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"