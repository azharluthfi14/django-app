from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def user_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile created')


@receiver(post_save, sender=User)
def user_save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
    print(f'Profile updated!')