from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Mysociallinks


def posts_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    posts = Post.newmanager.all()
    my = Mysociallinks.objects.first()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        posts = posts.filter(category=category)
    return render(request, 'index.html',    {'categories': categories,
                                             'category': category,
                                             'posts': posts,
                                             'my': my, })


def post_detail(request, id):
    my = Mysociallinks.objects.first()
    post = get_object_or_404(Post, id= id)
    return render(request, 'post_detail.html', {'post': post, 'my': my})

