from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Cathal Dolan',
        'title': 'Post 1',
        'content': 'Post 1\'s content',
        'date_posted': 'January 17th, 2021'
    },
    {
        'author': 'Liam Dolan',
        'title': 'Post 2',
        'content': 'Post 2\'s content',
        'date_posted': 'January 18th, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
