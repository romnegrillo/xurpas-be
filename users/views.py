from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from users.models import CustomUser
from users.serializers import CustomUserSerializer


@api_view(["GET"])
def api_test(request):
    return Response({"message": "Testing API."})


class UserListAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = "id"


class UserUpdateAPIView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = "id"

    def perform_update(self, serializer):
        serializer.save()


class UserDestroyAPIView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = "id"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class UserMultipleDestroyAPIView(APIView):
    def post(self, request):

        data = request.data
        user_ids = data.get("user_ids")

        if user_ids is not None:
            if len(user_ids) == 0:
                return Response({"message": "No user ids provided."}, status=400)

            deleted_ids = []
            unlisted_ids = []

            # Check first if all user_ids are in the database.
            for user_id in user_ids:
                try:
                    instance = CustomUser.objects.get(id=user_id)
                    print(instance)
                    instance.delete()

                    deleted_ids.append(user_id)
                except CustomUser.DoesNotExist:
                    unlisted_ids.append(user_id)

            if len(unlisted_ids) == 0:
                return Response({"message": f"Users with ids {deleted_ids} has been deleted."})
            else:
                return Response({"message": f"Users with ids {deleted_ids} has been deleted. Users with ids {unlisted_ids} is not in the database."})


        return Response({"message": "Parameter user_ids is required."})