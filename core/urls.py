from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogPostSitemap
from . import views



sitemaps = {
    'blog':BlogPostSitemap
}

urlpatterns = [
    path('', views.home, name='home'),
    path('advertising/', views.advertising, name='advertising'),
    path('architecture/', views.architecture, name='architecture'),
    path('fetch_pics/<str:type>',views.fetch_pics,name='fetch_pics'),
    path('blog/', views.blog, name='blog'),
    path('post/<str:slug>', views.post, name='post'),
    path('get_posts/', views.get_posts, name='get_posts'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]