from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

# Create your models here.
class HoistCraneBrand(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name}"

class HoistCrane(models.Model):
    photo = CloudinaryField('image', overwrite = True)
    brand = models.ForeignKey(HoistCraneBrand, on_delete = models.CASCADE, related_name = 'products')
    name = models.CharField(max_length = 100)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(HoistCrane, self).save(*args, **kwargs)

    class Meta:
        managed = True
        verbose_name = 'Hoist Crane'
        verbose_name_plural = 'Hoist Cranes'
        ordering = ['-date_added']