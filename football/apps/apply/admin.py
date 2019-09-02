from django.contrib import admin

from .models import ReferenceCode, Application


class ReferenceCodeAdmin(admin.ModelAdmin):
    list_filter = ('code', 'is_used')
    search_fields = ('code',)
    list_filter = ('is_used',)


admin.site.register(ReferenceCode, ReferenceCodeAdmin)
admin.site.register(Application)
