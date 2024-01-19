from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.
class Category(BaseModel):
    cat_name = models.CharField(max_length = 100, blank = False, null = False, default = "")
    def __str__(self):
        return self.cat_name

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Product(BaseModel):
    brand = models.CharField(max_length= 20, null = False, default="")
    Name = models.CharField(max_length = 100, null= False, default = "")
    description = models.TextField(max_length = 2000, null=False, default = "")
    category = models.ForeignKey(Category , on_delete = models.CASCADE)
    main_image = models.ImageField(upload_to="product/prod-main")
    price = models.DecimalField(max_digits = 6, decimal_places = 2 , default = "0")
    colors = models.ManyToManyField(Color, related_name='products', blank=True)
    images = models.ManyToManyField('Image')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Name)

        super().save(*args, **kwargs)
    def __str__(self):
        return self.Name




class Image(models.Model):
    image = models.ImageField(upload_to='product/prod-images')

    def __str__(self):
        return f"Image {self.pk}"