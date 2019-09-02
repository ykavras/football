from django.contrib import admin

from .models import ReferenceCode, Application


class ReferenceCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_used')
    search_fields = ('code',)
    list_filter = ('is_used',)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone', 'has_reference_code', 'confirm')
    search_fields = ('name', 'last_name', 'email', 'phone')
    list_filter = ('confirm', 'create_date')


admin.site.register(Application, ApplicationAdmin)
admin.site.register(ReferenceCode, ReferenceCodeAdmin)
