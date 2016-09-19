from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Todo

# Http 404 error when not in development
# get_object_or_404(Model, id=model_id) instead of Model.objects.get(id=model_id)

def todos_index(request):
    todos = Todo.all()
    return render(request, 'todos/index.html', {'todos': todos})

def todos_new(request):
    categories = Category.all()
    return render(request, 'todos/new.html', {'categories': categories})

# POST /todos/create
def todos_create(request):
    # import pdb; pdb.set_trace()
    params = request.POST

    # Create new todo is task given
    if params.get('todo[task]'):
        todo = Todo(task= params.get('todo[task]'))
        todo.save()

        # Create new category is category name
        if params.get('new_category[name]'):
            category = Category.objects.create(name=params.get('new_category[name]'))
            category_ids = map(int, params.getlist('todo[category_ids]')) + [category.id]
        else:
            category_ids = map(int, params.getlist('todo[category_ids]'))

        todo.categories = category_ids
        todo.save()

    return redirect('todos:index')

def todos_show(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todos/show.html', {'todo': todo})

def categories_index(request):
    categories = Category.all()
    return render(request, 'categories/index.html', {'categories': categories})

def categories_show(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'categories/show.html', {'category': category})
