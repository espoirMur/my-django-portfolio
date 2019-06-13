from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {'posts': posts}
    return render(request, 'blogs_index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category).all().order_by('-created_on')
    context = {'posts': posts, 'category': category}
    return render(request, 'blogs_category.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data()
            comment = Comment(author=form_data.get('author'),
                              body=form_data.get('body'),
                              post=post)
            comment.save()
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }
    return render(request, "blog_detail.html", context)
