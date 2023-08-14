from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from common.constants import roles
from common.serializers.mixins import DictMixinSerializer


class ExtendedView:
    multi_permission_classes = None
    multi_serializer_classes = None
    request = None

    def get_serializer_class(self):
        assert self.serializer_class or self.multi_serializer_classes, (
            '"%s" should either include `serializer_class`, '
            '`multi_serializer_class`, attribute or override the '
            '`get_serializer_class()` method' % self.__class__.__name__
        )
        if not self.multi_serializer_classes:
            return self.serializer_class
        # определение роли пользователя
        user = self.request.user
        if user.is_anonymous:
            user_roles = (roles.PUBLIC_GROUP)
        elif user.is_superuser:
            user_roles = (roles.ADMIN_GROUP)
        else:
            user_roles = set(user.group.all().value_list('code', flat=True))

        # action or method
        if hasattr(self, 'action') and self.action:
            action = self.action
        else:
            action = self.request.method
        # role + action
        for role in user_roles:
            serializer_key = f'{role}__{action}'
            if self.multi_serializer_classes.get(serializer_key):
                return self.multi_serializer_classes.get(serializer_key)

        # get role serializer
        for role in user_roles:
            serializer_key=role
            if self.multi_serializer_classes.get(serializer_key):
                return self.multi_serializer_classes.get(serializer_key)

        # get action serializer
        return self.multi_serializer_classes.get(action) or self.serializer_class



    def get_permissions(self):
        # define request method or action
        if hasattr(self, 'action'):
            action = self.action
        else:
            action = self.request.method

        if self.multi_permission_classes:
            permissions = self.multi_permission_classes.get(action)
            if permissions:
                return [permission() for permission in permissions]

        return [permission() for permission in self.permission_classes]




class ExtendedGenericViewSet(ExtendedView,GenericViewSet):
    pass



class ListViewSet(ExtendedGenericViewSet, mixins.ListModelMixin):
    pass

class DictListViewMixin(ListViewSet):
    serializer_class = DictMixinSerializer
    pagination_class = None

class LCRUViewSet(ExtendedGenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin):
    pass


class LCRUDViewSet(LCRUViewSet, mixins.DestroyModelMixin):
    pass


class ListCreateUpdateViewSet(ExtendedGenericViewSet,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,):
    pass