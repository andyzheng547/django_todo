from django.conf.urls import url
from . import views

app_name = 'todos'

urlpatterns = [
    # /todos
    url(r'^$', views.todos_index, name='index'),

    # /todos/:id
    url(r'^(?P<todo_id>[0-9]+)/?$', views.todos_show, name='show'),

    # /todos/categories
    url(r'^categories/?$', views.categories_index, name='categories_index'),

    # /todos/categories/:id
    url(r'^categories/(?P<category_id>[0-9]+)/?$', views.categories_show, name='categories_show')
]
