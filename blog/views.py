from django.shortcuts import render

from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    
    return render(request, 'blog/index.html', {'posts': posts})


def show(request, post_id):
    post = Post.objects.get(id=post_id)
    
    return render(request, 'blog/show.html', {'post': post})