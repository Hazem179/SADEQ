from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('advertising/', views.advertising, name='advertising'),
    path('architecture/', views.architecture, name='architecture'),
    path('fetch_pics/<str:type>',views.fetch_pics,name='fetch_pics'),
    path('blog/', views.blog, name='blog'),
    path('blogDetails/<str:id>', views.blogDetails, name='blogDetails'),
    path('get_posts/', views.get_posts, name='get_posts'),
]