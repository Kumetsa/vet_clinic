from django.urls import path

from vet_clinic.accounts.views import LoginUserView, CreateUserView, logout_user

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('logout/', logout_user, name='logout_user'),
]