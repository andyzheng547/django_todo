from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Todo(models.Model):
    task = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
