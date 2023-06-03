import markdown
from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth import get_user_model

from encrypted_model_fields.fields import EncryptedTextField


User = get_user_model()


class NotesQueryset(models.query.QuerySet):

    def for_user(self, user):
        return self.filter(owner=user)


class Note(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(editable=False, max_length=50)
    body = EncryptedTextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = NotesQueryset.as_manager()

    def as_html(self):
        md_extensions = ["codehilite", "nl2br", "fenced_code", "sane_lists", "wikilinks", "toc"]
        return mark_safe(
            markdown.markdown(self.body, extensions=md_extensions, output_format="html")
        )

    def as_pdf(self):
        """TODO: Allow users to download note as pdf"""
        pass

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-updated_at", "-created_at")


