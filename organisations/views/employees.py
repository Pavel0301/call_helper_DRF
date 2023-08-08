from drf_spectacular.utils import extend_schema_view, extend_schema
from common.views.mixins import CRUViewSet, CRUDViewSet, ListViewSet
from organisations.models.organisations import Organisation, Employee
from organisations.serializers.api import employees as employees_s


@extend_schema_view(
    list=extend_schema(summary='Список сотрудников организации', tags=['Организации: Сотрудники']),
    retrieve=extend_schema(summary='Деталка сотрудника организации', tags=['Организации: Сотрудники']),
    create=extend_schema(summary='Создать сотрудника организации', tags=['Организации: Сотрудники']),
    update=extend_schema(summary='Изменить сотруника организацим', tags=['Организации: Сотрудники']),
    partial_update=extend_schema(summary='Частичное изменение сотрудника организации', tags=['Организации: Сотрудники']),
    destroy=extend_schema(summary='Удалить сотрудника из организации ', tags=['Организации: Сотрудники']),
)

class EmployeeView(CRUDViewSet):
    queryset = Employee.objects.all()
    serializer_class  = employees_s.EmployeeListSerializer
    # переименование в роуте id в employee_id во избжания конфликта
    lookup_url_kwarg = 'employee_id'
    #
    def get_serializer_class(self):
        # if self.action == 'list':
        # return organisations.OrganisationListSerializer
        if self.action == 'retrieve':
            return employees_s.EmployeeRetrieveSerializer
        elif self.action == 'create':
            return employees_s.EmployeeCreateSerializer
        elif self.action == 'update':
            return employees_s.EmployeeUpdateSerializer
        elif self.action == 'partial_update':
            return employees_s.EmployeeUpdateSerializer
        elif self.action == 'destroy':
            return employees_s.EmployeeDestroySerializer
        return self.serializer_class

    def get_queryset(self):
        organisation_id = self.request.parser_context['kwargs'].get('pk')
        print(organisation_id)
        queryset = Employee.objects.filter(organisation_id=organisation_id)
        return queryset