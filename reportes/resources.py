# bug_report_resource.py

# from import_export import resources, fields, ValidationError
# from import_export.widgets import DateWidget
# from .models import BugReport

# class BugReportResource(resources.ModelResource):
#     # Define los campos del modelo BugReport que deseas importar
#     date_reported = fields.Field(column_name='date_reported', attribute='date_reported', widget=DateWidget(format='%d/%m/%Y'))

#     class Meta:
#         model = BugReport
#         skip_unchanged = True
#         report_skipped = False
#         import_id_fields = []  # Define esto como una lista vacía para evitar importar la columna "id"
#         fields = ('title', 'reported_by', 'date_reported', 'area', 'status', 'project_name', 'causal', 'link', 'assigned_to', 'severity')


# from import_export import resources, fields
# from import_export.widgets import DateWidget
# from django.core.exceptions import ValidationError  # Importa ValidationError de django.core.exceptions
# from .models import BugReport

# class BugReportResource(resources.ModelResource):
#     # Define los campos del modelo BugReport que deseas importar/exportar
#     date_reported = fields.Field(column_name='date_reported', attribute='date_reported', widget=DateWidget(format='%d/%m/%Y'))

#     class Meta:
#         model = BugReport
#         skip_unchanged = True
#         report_skipped = False
#         import_id_fields = []  # Define esto como una lista vacía para evitar importar la columna "id"
#         fields = ('title', 'reported_by', 'date_reported', 'area', 'status', 'project_name', 'causal', 'link', 'assigned_to', 'severity')

#     def before_import_row(self, row, **kwargs):
#         # Validación personalizada: asegurarse de que el campo 'title' no esté vacío
#         title = row.get('title')
#         if not title:
#             raise ValidationError("El campo 'title' no puede estar vacío.")

#     # Otras validaciones personalizadas pueden agregarse aquí

from import_export import resources, fields
from django.core.exceptions import ValidationError  # Importa ValidationError de django.core.exceptions
from import_export.widgets import DateWidget
from .models import BugReport

class BugReportResource(resources.ModelResource):
    date_reported = fields.Field(
        column_name='date_reported',
        attribute='date_reported',
        widget=DateWidget(format='%d/%m/%Y')
    )

    class Meta:
        model = BugReport
        skip_unchanged = True
        report_skipped = False
        import_id_fields = []  # Define esto como una lista vacía para evitar importar la columna "id"
        fields = ('title', 'reported_by', 'date_reported', 'area', 'status', 'project_name', 'causal', 'link', 'assigned_to', 'severity')
        list_per_page = 25

    def before_import_row(self, row, **kwargs):
        title = row.get('title')
        if not title:             
             raise ValidationError("El campo 'title' no puede estar vacío.")
        # Verifica que los valores de 'area', 'status', 'causal' y 'severity' estén en las opciones permitidas
        for field_name in ['area', 'status', 'causal', 'severity']:
            field_value = row.get(field_name)
            field_choices = dict(BugReport._meta.get_field(field_name).choices)
            if field_value not in field_choices:
                raise ValidationError(f"{field_name} no es una opción válida. Opciones permitidas: {', '.join(field_choices.keys())}")

    def import_row(self, row, instance_loader, **kwargs):
        # Realiza la importación normal, sin embargo, ya validaste los campos en before_import_row
        return super().import_row(row, instance_loader, **kwargs)

