from django.contrib import admin

from .models import ReferenceCode, Application


class ReferenceCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'total_usage')
    search_fields = ('code',)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone', 'has_reference_code', 'confirm')
    search_fields = ('name', 'last_name', 'email', 'phone')
    list_filter = ('confirm', 'create_date', 'reference_code__code')


admin.site.register(Application, ApplicationAdmin)
admin.site.register(ReferenceCode, ReferenceCodeAdmin)
