# Import the post_save signal from Django's model signals
from django.db.models.signals import post_save

# Import the built-in User model from Django's auth system
from django.contrib.auth.models import User

# Import the receiver decorator to link functions to signals
from django.dispatch import receiver

# Import the custom Profile model from the current app's models
from .models import Profile

# Connect the create_profile function to the post_save signal for the User model
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Check if the instance was newly created (not updated)
    if created:
        # If the User instance is new, create a corresponding Profile
        Profile.objects.create(user=instance)
        

# Connect the save_profile function to the post_save signal for the User model
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Save the associated Profile instance whenever the User instance is saved
    instance.profile.save()