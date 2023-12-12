from django.db import models

# Create your models here.
from django.db import models

from django.utils.text import slugify

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
  
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MenuItem, self).save(*args, **kwargs)
    def __str__(self):
        return self.name