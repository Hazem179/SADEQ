from turtle import pos
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from .models import Picture,Category,BlogPost
from .utils import filter_pictures,check_background_image

# Create your views here.
def home(request):
    bg = check_background_image()
    context = {'bg':bg}
    return render(request, 'site/home.html',context)


def architecture(request):
    return filter_pictures(request, '1', 'site/architecture.html')
def fetch_pics(request,type):
    if request.method == "GET":
        pictures = Picture.objects.filter(type=type)
        title_filter = request.GET.get('title')
        category_filter = request.GET.get('category')
        if title_filter and category_filter:
            pictures = pictures.filter(Q(title__icontains=title_filter) & Q(category__id=category_filter))
        elif title_filter:
            pictures = pictures.filter(title__icontains=title_filter)
        elif category_filter:
            pictures = pictures.filter(category__id=category_filter)
        pictures_data = {}
        for i, picture in enumerate(pictures):
            picture_data = {
                'title': picture.title,
                'image_url': picture.image.url,
            }
            pictures_data[i] = picture_data
    return JsonResponse({"pictures":pictures_data},safe=False)

def advertising(request):
    return filter_pictures(request, '2', 'site/advertising.html')


def blog(request):
    categories = Category.objects.all()
    posts = BlogPost.objects.all()
    context = {
        'categories':categories,
        'posts':posts,
    }
    return render(request, 'site/blog.html',context=context)


def blogDetails(request,id):
    blog_post =  BlogPost.objects.get(id =id)
    context = {
        "post":blog_post
    }
    return render(request, 'site/blogDetails.html',context=context)


def get_posts(request):
    posts = []
    category = request.GET.get('category')
    post_objects = BlogPost.objects.filter(category__id=category)
    for post in post_objects:
            post_data = {
                'title': post.title,
                'subtitle': post.subtitle,
                'body': post.body,
                'category_name': post.category.name,
                'category_type': post.category.type,
                'created_at':post.created_at,
                'image_url': post.post_image.url,
            }
            posts.append(post_data)
    print(posts)
    return JsonResponse(posts,safe=False)