from django.shortcuts import render
from .models import Post, Comment, Tag, Category


# Create your views here.


def home_view(request):
    objects = Post.objects.order_by('-id')
    comments = Comment.objects.all()
    categories = Category.objects.all()
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    tags = Tag.objects.all()
    tag = request.GET.get('tag')
    print(categories.get(id=4).post_set.all().count())
    if tag:
        objects = objects.filter(tag__tag__exact=tag)
    if cat:
        objects = objects.filter(category__category__exact=cat)
    if q:
        objects = objects.filter(title__icontains=q)
    context = {
        'objects': objects,
        'comments': comments,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'posts/index.html', context)


def last_3_posts_view(request):
    obj = Post.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    category = Category.objects.all()
    context = {
        'objects': obj,
        'tags': tags,
        'categories': category
    }
    return render(request, 'rside.html', context)


def single_post_view(request, slug):
    obj = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'object': obj,
        'tags': tags,
        'categories': categories
    }
    return render(request, 'posts/single.html', context)


def about_view(request):
    return render(request, 'posts/about.html')


def fashion_view(request):
    articles = Post.objects.order_by('-id').filter(type=0)

    context = {
        'objects': articles
    }

    return render(request, 'posts/fashion.html', context)


def travel_view(request):
    articles = Post.objects.order_by('-id').filter(type=1)

    context = {
        'objects': articles
    }

    return render(request, 'posts/fashion.html', context)