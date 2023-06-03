from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("notes_list_or_add"))),
    path("admin/", admin.site.urls),
    path("notes/", include("notes.urls")),
]
