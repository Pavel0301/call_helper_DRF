from django.contrib import admin

from breaks.models.replacements import GroupInfo
from organisations.models import organisations, groups, dicts
################################
# INLINES
################################
class EmployeeInline(admin.TabularInline): #(StackInline)
    model = organisations.Employee
    fields = ('user', 'position', 'date_joined',)

class MemberInline(admin.TabularInline): #(StackInline)
    model = groups.Member
    fields = ('user', 'date_joined',)

class ProfileBreakInline(admin.StackedInline): #(StackInline)
    model = GroupInfo
    fields = (
        'min_active', 'break_start', 'break_end', 'break_max_duration'
    )
    search_fields = ('group__name',)



################################
# MODELS
################################

@admin.register(organisations.Organisation)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director')

    filter_horizontal = ('employee',)
    inlines = (EmployeeInline,)

    readonly_fields = (
        'created_at', 'updated_at', 'created_by', 'updated_by',
    )

@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager',)

    list_display_links = ('id', 'name')

    search_fields = ('name',)  #search_fields = ('name__<options>',)

    inlines = (MemberInline, ProfileBreakInline,)
    readonly_fields = (
        'created_at', 'updated_at', 'created_by', 'updated_by',
    )


@admin.register(dicts.Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name', 'sort', 'is_active',
    )