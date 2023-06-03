import django_filters

from .models import Note


class NotesFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    @property
    def qs(self):
        notes = super().qs
        return notes.for_user(self.request.user)

    class Meta:
        model = Note
        fields = {
            "title": ["icontains"],
            "created_at": ["lt", "gt"],
            "updated_at": ["lt", "gt"]
        }
