
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User
from .serializers import UserSerializers


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializers

    def get_queryset(self):
        return User.objects.all().filter(username=self.request.user)



