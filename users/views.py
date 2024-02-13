from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from users.serializers import CustomUserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'Регистрация прошла успешно!'}, status=status.HTTP_201_CREATED)
    

