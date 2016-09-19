from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def todos(self):
        return self.todo_set.all().order_by('id')

    def todo_tasks(self):
        return self.todos().values_list('task', flat=True)

    def todo_ids(self):
        return self.todos().values_list('id', flat=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.name

    @classmethod
    def all(categories):
        return categories.objects.all().order_by('id')

    @classmethod
    def first(categories):
        return categories.objects.order_by('id').first()

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

    def category_names(self):
        return self.categories.values_list('name', flat=True)

    def category_ids(self):
        return self.categories.values_list('id', flat=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.task + ' - ' + self.completed()

    @classmethod
    def all(todos):
        return todos.objects.all().order_by('id')

    @classmethod
    def first(todos):
        return todos.objects.order_by('id').first()

    @classmethod
    def last(todos):
        return todos.objects.latest('id')

    class Meta:
        ordering = ('task', 'status')
        verbose_name_plural = 'todos'
