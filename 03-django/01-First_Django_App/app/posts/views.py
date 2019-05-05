from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.

def index(request):

    posts = Posts.objects.all()[:10]

    # list = [1, 2, 3]
    # list[::-1] > [3, 2, 1]
    # list[1:2] > [2, 3]

    content = {
        'title': 'Django is Amazing',
        'posts': posts
    }

    return render(request, "posts/index.html", content)