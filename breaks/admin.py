from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html

from breaks.models import replacements, dicts, breaks


################################
# INLINES
################################
class ReplacementEmployeeInline(admin.TabularInline): #(StackInline)
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status',)









################################
# MODELS
################################


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'date', 'break_start', 'break_end', 'break_max_duration',)

    inlines = (
        ReplacementEmployeeInline,
    )

    #autocomplete_fields = ('group',) # работет по GroupAdmin.search_fields


@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active')

    #field = ('<field_name>') скрывает поле
    #exclude = ('<field_name>', '<field_name>') скрывает поля переданные в параметры


@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active')

@admin.register(replacements.ReplacementEmployee)
class ReplacementEmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee', 'replacement', 'status')

@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = ('id', 'replacement_link', 'status', 'break_start', 'break_end')

    #list_filter = ('status__name',)

    list_filter = ('status',)

    radio_fields = {'status': admin.HORIZONTAL} # удобное отображение полей например BooleanField admin.VERTICAL

    empty_value_display = 'unknown' # null поля в админке принимают значение unknown
    # <field_name>.empty_value_display = '...'

    #readonly_fields = ('created_at', 'updated_at')

    # удобный способ создания ссылок как атрибуты в админке
    def replacement_link(self, obj):
        link = reverse('admin:breaks_replacement_change', args=[obj.replacement.id])
        return format_html('<a href="{}">{}</a>', link, obj.replacement)


