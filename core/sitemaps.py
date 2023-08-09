from django.contrib.sitemaps import Sitemap
from .models import BlogPost
 
 
class BlogPostSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.created_at
        
    def location(self,obj):
        return '/post/%s' % (obj.slug)