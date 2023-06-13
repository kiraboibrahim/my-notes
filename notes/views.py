from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django_filters.views import FilterView

from .models import Note
from .forms import AddNoteForm, EditNoteForm
from .filters import NotesFilter
from .mixins import NoteOwnerRequiredMixin


class NoteListOrAddView(LoginRequiredMixin, SuccessMessageMixin, FilterView):
    model = Note
    template_name = "notes/notes_list.html"
    extra_context = {
        "add_note_form": AddNoteForm(),
        "edit_note_form": EditNoteForm,
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


class NoteEditView(LoginRequiredMixin, NoteOwnerRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Note
    form_class = EditNoteForm
    template_name = "notes/notes_list.html"
    extra_context = {
        "add_note_form": AddNoteForm(),
        "edit_note_form": EditNoteForm(),
    }
    success_message = "Your note has been updated"

    def form_invalid(self, form):
        notes = self.get_queryset().for_user(self.request.user)
        context = self.get_context_data()
        context.update({"edit_note_form": form, "notes": notes})
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse("notes_list_or_add")

    def get(self, request, **kwargs):
        return redirect(reverse("notes_list_or_add"))


class NoteDeleteView(LoginRequiredMixin, NoteOwnerRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Note
    http_method_names = ["get"]
    success_url = reverse_lazy("notes_list_or_add")
    success_message = "Your note has been deleted"

    def get(self, request, *args, **kwargs):
        # Don't redirect to delete confirmation page, Confirmation already handled by the frontend, Just immediately
        # delete note
        response = self.delete(request, *args, **kwargs)
        messages.success(request, self.get_success_message({}))
        return response
