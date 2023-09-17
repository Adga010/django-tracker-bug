from import_export import resources, fields
from django.core.exceptions import ValidationError  # Importa ValidationError de django.core.exceptions
from import_export.widgets import DateWidget
from .models import BugReport

class BugReportResource(resources.ModelResource):
    # Definiciones de campos
    date_reported = fields.Field(
        column_name='date_reported',
        attribute='date_reported',
        widget=DateWidget(format='%d/%m/%Y')
    )

    # Definiciones de opciones
    class Meta:
        model = BugReport
        skip_unchanged = True
        report_skipped = False
        import_id_fields = []  # Define esto como una lista vacía para evitar importar la columna "id"
        fields = ('title', 'reported_by', 'date_reported', 'area', 'status', 'project_name', 'causal', 'link', 'assigned_to', 'severity')
        list_per_page = 25

    # Función para validar antes de importar una fila
    def before_import_row(self, row, **kwargs):
        # Validación del campo 'title'
        title = row.get('title')
        if not title:
            raise ValidationError("El campo 'title' no puede estar vacío.")
    
    # Validación adicional: Comprobar si el campo 'title' comienza con 'BUG'
        if not title.startswith('BUG'):
            raise ValidationError("El campo 'title' debe comenzar con 'BUG'.")
    
        
        # Verificación de valores en campos 'area', 'status', 'causal' y 'severity'
        for field_name in ['area', 'status', 'causal', 'severity']:
            field_value = row.get(field_name)
            field_choices = dict(BugReport._meta.get_field(field_name).choices)
            if field_value not in field_choices:
                raise ValidationError(f"{field_name} no es una opción válida. Opciones permitidas: {', '.join(field_choices.keys())}")
            
        # Validación personalizada para 'date_reported'
        date_reported = row.get('date_reported')
        if date_reported is None:
            raise ValidationError("El campo 'date_reported' es obligatorio. Asegúrate de proporcionar una fecha válida en el formato dd/mm/yyyy.")
        # Validación personalizada para 'date_reported'
        date_reported = row.get('project_name')
        if date_reported is None:
            raise ValidationError("El campo 'project_name' es obligatorio.")
        # Validación personalizada para 'link'
        date_reported = row.get('link')
        if date_reported is None:
            raise ValidationError("El campo 'link' es obligatorio.")
        # Validación personalizada para 'assigned_to'
        date_reported = row.get('assigned_to')
        if date_reported is None:
            raise ValidationError("El campo 'assigned_to' es obligatorio.")
         # Validación personalizada para 'link'
        date_reported = row.get('reported_by')
        if date_reported is None:
            raise ValidationError("El campo 'reported_by' es obligatorio.")

   # Función para importar una fila
    def import_row(self, row, instance_loader, **kwargs):
        # Realiza la importación normal, ya que los campos se validaron en before_import_row
        return super().import_row(row, instance_loader, **kwargs)