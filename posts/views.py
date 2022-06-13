from django.shortcuts import render
from django.utils import timezone
from .models import Post, Folder
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request, pk):
    posts = Post.objects.filter(published_date__lte=timezone.now(), folder=pk).order_by('-published_date')
    return render(request, 'posts/post_list.html', {'posts' : posts})

def folder_list(request):
    folders = Folder.objects.all()
    return render(request, 'posts/folder_list.html', {'folders' : folders})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # Eviter d'afficher une page vide
    return render(request, 'posts/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form})

