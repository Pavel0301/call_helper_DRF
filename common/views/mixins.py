from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ExtendedGenericViewSet(GenericViewSet):
    pass



class ListViewSet(ExtendedGenericViewSet, mixins.ListModelMixin):
    pass



class CRUViewSet(ExtendedGenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin):
    pass


class CRUDViewSet(CRUViewSet, mixins.DestroyModelMixin)