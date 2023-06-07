from django.contrib import admin
from .models import Software, SoftwareType

@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('user', 'type_of_software', 'soft_name', 'soft_version')
    # outros campos a serem exibidos na lista de objetos

@admin.register(SoftwareType)
class SoftwareTypeAdmin(admin.ModelAdmin):
    list_display = ('type_id', 'description')
    # outros campos a serem exibidos na lista de objetos
