from django.db import models

# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=True)
    icon = models.ImageField(upload_to='section_ico', blank=True)
    image = models.ImageField(upload_to='section_img', blank=True)

    def __str__(self):
        return self.title
