from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
# Register your models here.

admin.site.unregister(Group)

admin.site.register(Picture)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','type','description')
    search_fields = ('name','type')
    exclude = ('slug',)

admin.site.register(Category,CategoryAdmin)


class BackGroundImageModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        # Disable deleting for all instances of YourModel
        return False
admin.site.register(BackgroundImage,BackGroundImageModelAdmin)




class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','category','created_at')
    search_fields = ('name','category')
    
admin.site.register(BlogPost,BlogPostAdmin)
