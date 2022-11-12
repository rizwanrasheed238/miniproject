# from distutils.command.upload import upload
# from email.mime import image
# from hashlib import new
# from pydoc import describe
# from telnetlib import STATUS
# from unicodedata import name
from unicodedata import category
from django.db import models
import datetime
import os


def getFileName(requset, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)


class Catagory(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    slug=models.SlugField(max_length=250,null=True,blank=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, editable=False)
    description = models.TextField(max_length=500, null=True, blank=False)
    status = models.BooleanField(default=False, null=True, help_text="0=show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    Subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    slug = models.SlugField(max_length=250, null=True, blank=True, editable=False)
    product_image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    updated=models.DateTimeField(auto_now=True)
    trending = models.BooleanField(default=False, help_text="0=default,1-Trending")
    modified_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{}' .format(self.name)




