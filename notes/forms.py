from django import forms

from .models import Note


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
            "body": forms.Textarea(attrs={"id":  "note_body"})
        }


class EditNoteForm(AddNoteForm):

    def save(self, commit=True):
        return self._meta.model(**self.cleaned_data).save(commit)
