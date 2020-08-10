from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.views.generic import CreateView
from .forms import PostForm
from django.urls import reverse_lazy

from django.shortcuts import redirect

def index(request):
    latest = Post.objects.all()[:11]
    return render(request, 'index.html', {'posts': latest})

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            group = form.cleaned_data['group']
            text = form.cleaned_data['text']
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'new.html', {'form': form})
