from django.shortcuts import render
from .models import Category, Todo

def todos_index(request):
    todos = Todo.all()
    return render(request, 'todos/index.html', {'todos': todos})

def todos_show(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todos/show.html', {'todo': todo})

def categories_index(request):
    categories = Category.all()
    return render(request, 'categories/index.html', {'categories': categories})
