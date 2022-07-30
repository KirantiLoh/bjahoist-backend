from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

# Create your models here.
class CargoLift(models.Model):
    photo = CloudinaryField('image', overwrite = True)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CargoLift, self).save(*args, **kwargs)

    class Meta:
        managed = True
        verbose_name = 'Cargo Lift'
        verbose_name_plural = 'Cargo Lifts'
        ordering = ['-date_added']