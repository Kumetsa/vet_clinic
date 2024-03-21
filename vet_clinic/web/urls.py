from django.urls import path

from vet_clinic.web.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]