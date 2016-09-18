from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def todos(self):
        return self.todo_set.all()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

class Todo(models.Model):
    task = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.task

    def completed(self):
        return self.status

    class Meta:
        ordering = ('task', 'status')
        verbose_name_plural = 'todos'
