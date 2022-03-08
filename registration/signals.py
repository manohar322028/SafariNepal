from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Profile,Preferences

import os


@receiver(post_delete, sender=Profile)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if (instance.profile_pic.path)=='defaultpp.jpg':
            return False
    if instance.profile_pic:
        if os.path.isfile(instance.profile_pic.path):
            os.remove(instance.profile_pic.path)

@receiver(pre_save, sender=Profile)
def auto_delete_image_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Profile.objects.get(pk=instance.pk).profile_pic
        if (old_file.path)=='defaultpp.jpg':
            return False
    except Profile.DoesNotExist:
        return False

    new_file = instance.profile_pic
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)