from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})

def result(request):
    return render(request, 'result.html')

def search(request):
    return render(request, 'search.html')
