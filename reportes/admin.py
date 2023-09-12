# from django.contrib import admin
# from .models import BugReport

# class BugReportAdmin(admin.ModelAdmin):
#     list_display = ('title', 'project_name', 'severity' ,'causal', 'status', 'assigned_to')
#     list_filter = ('project_name', 'area')
#     search_fields = ['project_name']
#     date_hierarchy = 'date_reported'  # Agrega un filtro de fechas para el campo 'date_reported'

# # Registra el modelo BugReport con la personalización BugReportAdmin
# admin.site.register(BugReport, BugReportAdmin)

# admin.py

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 
from .models import BugReport
from .resources import BugReportResource  # Asegúrate de importar tu recurso definido en resources.py

# Cambia el nombre del panel de administración
admin.site.site_header = 'Panel de Administración de Bugs - Cadena'

class BugReportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'project_name', 'severity', 'causal', 'status', 'assigned_to')
    list_filter = ('project_name', 'area')
    date_hierarchy = 'date_reported'  # Agrega un filtro de fechas para el campo 'date_reported'
    search_fields = ['project_name']
    resource_class = BugReportResource  # Asocia el recurso a la vista de administración

    # ... (otras configuraciones de tu modelo)

# Registra el modelo BugReport con la personalización BugReportAdmin
admin.site.register(BugReport, BugReportAdmin)