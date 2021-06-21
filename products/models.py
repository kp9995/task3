from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Products(models.Model):

    name = models.CharField(max_length=55, blank=False)
    description = models.CharField(max_length=250, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', related_name='products',null=True,on_delete=models.SET_NULL)
    thumbnail = models.ImageField(upload_to='products/thumbnail',null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'

    def get_absolute_url(self):
        return reverse('products:productdetails',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created']


class Category(models.Model):

    name = models.CharField(max_length=55, blank=False, unique=True)
    slug = models.SlugField(max_length=55, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
        
    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save()

    def get_absolute_url(self):
        return reverse('products:shop_by_category', kwargs={'category_slug':self.slug})
            

class Images(models.Model):

    image_path = models.ImageField(upload_to='products')
    product = models.ForeignKey(Products, related_name='images', null=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'image'

    def __str__(self):
        return self.image_path.url