from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from .models import Post, Folder
from .forms import FolderForm, PostForm



def post_list(request, folder_pk):
    posts = Post.objects.filter(published_date__lte=timezone.now(), folder=folder_pk).order_by('-published_date')
    folder = Folder.objects.get(pk=folder_pk)
    return render(request, 'posts/post_list.html', {'posts' : posts, 'folder' : folder})

def folder_list(request):
    folders = Folder.objects.all()
    return render(request, 'posts/folder_list.html', {'folders' : folders})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # Eviter d'afficher une page vide
    return render(request, 'posts/post_detail.html', {'post': post})

def folder_edit(request, pk):
    folder = get_object_or_404(Folder, pk=pk)
    if request.method == "POST":
        form = FolderForm(request.POST, instance=folder)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.save()
            return redirect('folder_list')
    else:
        form = FolderForm(instance=folder)
    return render(request, 'posts/folder_edit.html', {'form': form})

def folder_new(request):
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.save()
            return redirect('folder_list')
    else:
        form = FolderForm()
    return render(request, 'posts/folder_new.html', {'form': form})

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


class FolderDeleteView(DeleteView):
    template_name = 'posts/folder_delete.html'
    model = Folder
    success_url = reverse_lazy('folder_list',)
    

class PostDeleteView(DeleteView):
    template_name = 'posts/post_delete.html'
    model = Post

    # cette fonction permet d'indiquer à la delete view dans quel liste d'objets
    # il doit aller rechercher la clé primaire qui lui a été transmise dans l'URL
    # http://127.0.0.1:8000/folder/post/delete/18/
    # Ici, on indique qu'il faut aller chercher dans l'ensemble des objets de la table Post
    # l'objet qui correspond à clé primaire 18.
    # Cette fonction est utile si on a pas défini la variable Model(l.83)
    # ou si on veut limiter la liste d'objets utlisée.
    
    # def get_queryset(self):
    #     queryset = Post.objects.all()
    #     return queryset
    
    def get_success_url(self):
        pk_folder = int(self.object.folder.pk)
        url = reverse_lazy("post_list", args=[pk_folder])
        return url 
    