from django.urls import path

from vet_clinic.web.views import IndexView, MyPetsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/my_pets/', MyPetsView.as_view(), name='my_pets'),
]