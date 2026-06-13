from django.shortcuts import get_object_or_404, redirect, render

from blog.forms import PostForm
from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.select_related('author').prefetch_related('tags').all()
    
    return render(request, 'blog/index.html', {'posts': posts})


def show(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related('author').prefetch_related('comments', 'tags'),
        id=post_id,
    )
    
    return render(request, 'blog/show.html', {'post': post})


def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save()
        return redirect('show', post_id=post.id)

    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Create Post'})


def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        post = form.save()
        return redirect('show', post_id=post.id)

    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Update Post'})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})
