from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django_filters.views import FilterView

from .models import Note
from .forms import AddNoteForm
from .filters import NotesFilter


class NoteListOrAddView(SuccessMessageMixin, FilterView):
    template_name = "notes/notes_list.html"
    extra_context = {
        "add_note_form": AddNoteForm()
    }
    context_object_name = "notes"
    http_method_names = ["get", "post"]
    success_message = "Your note has been created"
    filterset_class = NotesFilter

    def post(self, request, *args, **kwargs):
        note = None
        add_note_form = AddNoteForm(request.POST)
        self.object_list = self.get_queryset()
        if add_note_form.is_valid():
            note = add_note_form.save(request.user)
            messages.success(self.request, self.get_success_message(add_note_form.cleaned_data))
        return self.render_to_response(self.get_context_data(note=note, add_note_form=add_note_form))


class NoteEditView(SuccessMessageMixin, UpdateView):
    model = Note
    template_name = "notes/notes_list.html"
    extra_context = {
        "add_note_form": AddNoteForm()
    }
    success_message = "Your note has been updated"

    def get_success_url(self):
        return reverse("note_detail", args=(self.object.slug, ))

    def get(self, request, **kwargs):
        return redirect(reverse("notes_list_or_add"))


class NoteDeleteView(SuccessMessageMixin, DeleteView):
    model = Note
    success_url = reverse_lazy("notes_list")
    success_message = "Your note has been deleted"
