from django import forms

from .models import Note
from .filters import NotesFilter


class AddNoteForm(forms.ModelForm):

    def save(self, note_owner, commit=False):
        note = super().save(commit)
        note.owner = note_owner
        note.save()
        return note

    class Meta:
        model = Note
        fields = "__all__"
        exclude = ("owner", )
        widgets = {
            "body": forms.Textarea(attrs={"id":  "add-note-form__note-body"})
        }


class EditNoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = "__all__"
        exclude = ("owner", )
        widgets = {
            "title": forms.TextInput(attrs={"id": "edit-note-form__note-title"}),
            "body": forms.Textarea(attrs={"id":  "edit-note-form__note-body"})
        }


notes_filter_form = NotesFilter().form
