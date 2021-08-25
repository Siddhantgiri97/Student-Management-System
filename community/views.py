from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post, Comment
from .forms import AddPostForm, AddCommentForm
# Create your views here.


def home(request):
    allPosts = Post.objects.all().order_by('-date')
    context = {'allPosts': allPosts}
    return render(request, "community/community.html", context)


def view_post(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post).order_by('-timestamp')

    if request.method == 'POST':
        form = AddCommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            form = AddCommentForm()
    else:
        form = AddCommentForm()
    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, "community/post.html", context)


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
        return redirect('community:home')
    else:
        form = AddPostForm()
    context = {'form': form}
    return render(request, 'community/addPost.html', context)


def add_comment(request):
    if request.method == 'POST':
        form = AddCommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return redirect('community:home')
    else:
        form = AddCommentForm()
    context = {'form': form}
    return render(request, 'community/post.html', context)


def search_post(request):
    query = request.GET.get('search')
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(body__icontains=query)).order_by('-date')

    context = {'results': results, 'query': query}
    return render(request, 'community/search.html', context)
