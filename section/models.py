from django.db import models

# Create your models here.
class MainSection(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='section_img', blank=True)

    def __str__(self):
        return self.title

class AboutSection(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=True)
    icon = models.ImageField(upload_to='section_ico', blank=True)

    def __str__(self):
        return self.title


class Catalog(models.Model):
    title = models.CharField(max_length=80, blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        verbose_name=u'Image', upload_to="category_pic", blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        verbose_name=u'Image', upload_to="product_pic", blank=True)
    catalog = models.ForeignKey(Catalog)
    description = models.TextField(blank=True, help_text="Describe product")
    price = models.DecimalField(max_digits=15, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=15, decimal_places=2, null=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
