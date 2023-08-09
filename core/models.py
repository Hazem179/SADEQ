from django.db import models
from django.utils.text import slugify
import datetime
# Create your models here.


TYPES = ('1','architecture'),('2','advertising')

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='اسم الفئة')
    type = models.CharField(max_length=100,choices=TYPES,verbose_name='التصنيف')
    slug = models.SlugField(max_length=100)
    description = models.TextField(verbose_name='الوصف',blank=True,null=True)

    class Meta:
        verbose_name = 'الفئة'
        verbose_name_plural = 'الفئات'


    def __str__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان الصورة')
    image = models.ImageField(upload_to='images/',verbose_name='الصورة')
    type = models.CharField(max_length=100,choices=TYPES,verbose_name='التصنيف')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='الفئة')
    class Meta:
        verbose_name = 'الصورة'
        verbose_name_plural = 'الصور'
    def __str__(self):
        return self.title

class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='background_images/',verbose_name='صورة الخلفية',default='background_images/bg1.jpg')
    class Meta:
        verbose_name = 'صورة الخلفية'
        verbose_name_plural = 'صور الخلفية'
    
    def __str__(self):
        return self.image

class BlogPost(models.Model):
    title = models.CharField(max_length=128,verbose_name='عنوان المنشور')
    slug = models.SlugField(max_length=100,blank=True,verbose_name="الرابط")
    subtitle = models.CharField(max_length=64,verbose_name='العنوان الفرعي')
    body = models.TextField(verbose_name="محتوى المنشور")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="التصنيف")
    post_image = models.ImageField(upload_to='post_images/',verbose_name='صورة المنشور')
    created_at = models.DateField(default=datetime.date.today,verbose_name = "تاريخ إضافة المنشور")
    class Meta:
        verbose_name = 'منشور'
        verbose_name_plural = 'المنشورات'


    def save(self, *args, **kwargs):
        title = self.title
        self.slug = slugify(title, allow_unicode=True)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title