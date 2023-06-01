from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Note


@receiver(pre_save, sender=Note)
def populate_note_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)

