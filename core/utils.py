from django.db.models import Q
from django.http import QueryDict
from django.shortcuts import render
from django.conf import settings
from .models import *
from django.core.paginator import Paginator



def check_background_image():
    bg = BackgroundImage.objects.last()
    return bg.image.url

def filter_pictures(request, type, template_name):
    bg = check_background_image()
    categories = Category.objects.filter(type=type)
    pictures = Picture.objects.filter(type=type)
    base_url = request.path_info
    title_filter = request.GET.get('title')
    category_filter = request.GET.get('category')
    if title_filter and category_filter:
        pictures = pictures.filter(Q(title__icontains=title_filter) & Q(category__id=category_filter))
    elif title_filter:
        pictures = pictures.filter(title__icontains=title_filter)
    elif category_filter:
        pictures = pictures.filter(category__id=category_filter)
    paginator = Paginator(pictures, 7)
    page_number = request.GET.get('page')
    pictures_per_page = paginator.get_page(page_number)
    filter_params = QueryDict(mutable=True)
    if title_filter:
        filter_params['title'] = title_filter
    if category_filter:
        filter_params['category'] = category_filter
    pagination_urls = {}
    for num in pictures_per_page.paginator.page_range:
        filter_params['page'] = num
        pagination_urls[num] = f"{base_url}?{filter_params.urlencode()}"
    context = {
        'pictures': pictures_per_page,
        'pagination_urls': pagination_urls,
        'title_filter': title_filter,
        'category_filter': category_filter,
        'categories': categories,
        'bg':bg,
    }
    return render(request, template_name, context)



