from django.contrib import admin
from breaks.models import organisations, groups, replacements

################################
# INLINES
################################
class ReplacementEmployeeInline(admin.TabularInline): #(StackInline)
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status',)








################################
# MODELS
################################

@admin.register(organisations.Organisation)
class OrganizationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director')

@admin.register(groups.Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active',)



@admin.register(replacements.Replacement)
class ReplacementModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'date', 'break_start', 'break_end', 'break_max_duration',)

    inlines = (
        ReplacementEmployeeInline,
    )


@admin.register(replacements.ReplacementStatus)
class ReplacementStatusModelAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active')


@admin.register(replacements.ReplacementEmployee)
class ReplacementEmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('employee', 'replacement', 'status')

