from drf_spectacular.utils import extend_schema_view, extend_schema

from common.views.mixins import DictListViewMixin, ListViewSet, CRUViewSet
from organisations.models.dicts import Position
from organisations.models.organisations import Organisation
from organisations.serializers.api import organisations


@extend_schema_view(
    list=extend_schema(summary='Список организаций Search', tags=['Словари']),

)
class OrganisationSearchView(ListViewSet):
    queryset = Organisation.objects.all()
    serializer_class = organisations.OrganisationSearchSerializer


@extend_schema_view(
    list=extend_schema(summary='Список организаций Search', tags=['Организации']),
    retrieve=extend_schema(summary='Деталка организаций', tags=['Организации']),
    create=extend_schema(summary='Создать организацию', tags=['Организации']),
    update=extend_schema(summary='Изменить организацию', tags=['Организации']),
    partial_update=extend_schema(summary='Частичное изменение организации', tags=['Организации']),

)
class OrganisationView(CRUViewSet):
    queryset = Organisation.objects.all()
    serializer_class = organisations.OrganisationListSerializer



    def get_serializer_class(self):
        #if self.action == 'list':
           # return organisations.OrganisationListSerializer
        if self.action == 'retrieve':
            return organisations.OrganisationRetrieveSerializer
        elif self.action == 'create':
            return organisations.OrganisationCreateSerializer
        elif self.action == 'update':
            return organisations.OrganisationUpdateSerializer
        elif self.action == 'partial_update':
            return organisations.OrganisationUpdateSerializer

        return self.serializer_class

