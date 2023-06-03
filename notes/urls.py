from django.urls import path

from . import views as note_views

urlpatterns = [
    path("", note_views.NoteListOrAddView.as_view(), name="notes_list_or_add"),
    path("<slug:slug>/edit", note_views.NoteEditView.as_view(), name="note_edit"),
    path("<slug:slug>/delete", note_views.NoteDeleteView.as_view(), name="note_delete"),
]
