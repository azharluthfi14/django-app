from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pict_user')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            size_output = (300, 300)
            img.thumbnail(size_output)
            img.save(self.image.path)


class PredResults(models.Model):
    fixed_acidity = models.FloatField()
    volatile_acidity = models.FloatField()
    citric_acid = models.FloatField()
    residual_sugar = models.FloatField()
    chlorides = models.FloatField()
    free_sulfur_dioxide = models.FloatField()
    total_sulfur_dioxide = models.FloatField()
    density = models.FloatField()
    pH = models.FloatField()
    sulphates = models.FloatField()
    alcohol = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification