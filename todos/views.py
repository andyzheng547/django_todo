from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1>This is the Todos homepage</h1>")
