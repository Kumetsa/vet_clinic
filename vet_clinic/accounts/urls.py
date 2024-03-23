from django.urls import path, include

from vet_clinic.accounts.views import (LoginUserView, CreateUserView, logout_user, ProfileEditView,
                                       ProfileDetailsView, ProfileDeleteView)

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('logout/', logout_user, name='logout_user'),

    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='details_profile'),
        path('update/', ProfileEditView.as_view(), name='edit_profile'),
        path('delete/', ProfileDeleteView.as_view(), name='delete_profile'),
    ])),
]
