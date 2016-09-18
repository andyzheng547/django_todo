from django.conf.urls import url
from . import views

urlpatterns = [
    # /todos
    url(r'^$', views.todos_index, name='todos_index'),

    # /todos/:id
    url(r'^(?P<todo_id>[0-9]+)/?$', views.todos_show, name='todos_show'),

    url(r'^categories/?', views.categories_index, name='categories_index')
]
