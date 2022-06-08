from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users import views

urlpatterns = [
    path("users/test", views.api_test),

    path("login/", obtain_auth_token),

    path("users/list/", views.UserListAPIView.as_view()),
    path("users/create/", views.UserCreateAPIView.as_view()),
    path("users/retrieve/<int:id>/", views.UserRetrieveAPIView.as_view()),
    path("users/update/<int:id>/", views.UserUpdateAPIView.as_view()),
    path("users/delete/<int:id>/", views.UserDestroyAPIView.as_view()),
    path("users/delete/multiple/", views.UserMultipleDestroyAPIView.as_view()),
]
