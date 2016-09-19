from django.shortcuts import render, get_object_or_404
from .models import Category, Todo

# Http 404 error when not in development
# get_object_or_404(Model, id=model_id) instead of Model.objects.get(id=model_id)

def todos_index(request):
    todos = Todo.all()
    return render(request, 'todos/index.html', {'todos': todos})

def todos_show(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todos/show.html', {'todo': todo})

def categories_index(request):
    categories = Category.all()
    return render(request, 'categories/index.html', {'categories': categories})

def categories_show(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'categories/show.html', {'category': category})
