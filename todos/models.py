from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def todos(self):
        return self.todo_set.all()

    def __str__(self):
        return self.name

    @classmethod
    def all(categories):
        return categories.objects.all()

    @classmethod
    def first(categories):
        return categories.objects.first()

    @classmethod
    def last(categories):
        return categories.objects.latest('id')

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

class Todo(models.Model):
    task = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)

    def completed(self):
        completion_status = 'Complete' if self.status else 'Incomplete'
        return completion_status

    def __str__(self):
        return self.task + ' - ' + self.completed()

    @classmethod
    def all(todos):
        return todos.objects.all()

    @classmethod
    def first(todos):
        return todos.objects.first()

    @classmethod
    def last(todos):
        return todos.objects.latest('id')

    class Meta:
        ordering = ('task', 'status')
        verbose_name_plural = 'todos'
