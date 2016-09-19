from django.conf.urls import url
from . import views

app_name = 'todos'

urlpatterns = [
    # GET /todos
    url(r'^$', views.todos_index, name='index'),

    # GET /todos/:id
    url(r'^(?P<todo_id>[0-9]+)/?$', views.todos_show, name='show'),

    # GET /todos/new
    url(r'^new/?$', views.todos_new, name='new'),

    # POST /todos/create
    url(r'^create/?$', views.todos_create, name='create'),

    # GET /todos/categories
    url(r'^categories/?$', views.categories_index, name='categories_index'),

    # GET /todos/categories/:id
    url(r'^categories/(?P<category_id>[0-9]+)/?$', views.categories_show, name='categories_show')
]
