import pdb

from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from common.views.mixins import ListViewSet
from users.permissions import IsNotCorporate
from users.serializers.api import users as user_s

User = get_user_model()

@extend_schema_view(
    post=extend_schema(summary='Регистрация пользователя', tags=['Авторизация и Аутентификация'])
)
class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = user_s.RegistrationSerializer


@extend_schema_view(
    post=extend_schema(request=user_s.ChangePasswordSerializer, summary='Смена пароля', tags=['Авторизация и Аутентификация'])
)
class ChangePasswordView(APIView):

    def post(self, request):
        user = request.user
        serializer = user_s.ChangePasswordSerializer(
            instance=user, data=request.data
        )
        #pdb.set_trace()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)


@extend_schema_view(
    get=extend_schema(request=user_s.MeSerializer, summary='Профиль пользователя', tags=['Пользователи']),
    put=extend_schema(request=user_s.MeUpdateSerializer, summary='Изменить профиль пользователя', tags=['Пользователи']),
    patch=extend_schema(request=user_s.MeUpdateSerializer, summary='Изменить частично профиль пользователя', tags=['Пользователи'])
)
class MeView(RetrieveUpdateAPIView):
    permission_classes = [IsNotCorporate]
    queryset = User.objects.all()
    serializer_class = user_s.MeSerializer
    http_method_names = ('get', 'patch')
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return user_s.MeUpdateSerializer
        return user_s.MeSerializer

    def get_object(self):
        return self.request.user



@extend_schema_view(
    list=extend_schema(summary='Список пользователей Search', tags=['Пользователи']),

)
class UserListSearchView(ListViewSet):
    # убрать из списка суперюзеров
    queryset = User.objects.all()
    serializer_class = user_s.UserSearchListSerializer
