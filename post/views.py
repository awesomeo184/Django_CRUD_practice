from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from post.forms import PostForm
from post.models import Post


def list(request):
    query_set = Post.objects.all()
    context = {
        'posts': query_set
    }
    return render(request, 'post/list.html', context)


def detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'post/detail.html', context)


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            post.save()
            pk = post.id
            url = reverse('post:detail', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'post/create.html', context)
