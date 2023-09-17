from django.db import models

class BugReport(models.Model):
    STATUS_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Finalizado', 'Finalizado'),
    ]

    CAUSAL_CHOICES = [
        ('Desarrollo', 'Desarrollo'),
        ('Documentacion', 'Documentacion'),
        ('Testing', 'Testing'),
        ('Diseño', 'Diseño'),
        ('Analisis', 'Analisis'),
    ]

    SEVERITY_CHOICES = [
        ('Bloqueante', 'Bloqueante'),
        ('Funcional', 'Funcional'),
        ('Presentacion', 'Presentacion'),
    ]
    
    AREA_CHOICES = [
        ('AXCES', 'AXCES'),
        ('Gestion Del Riesgo', 'Gestion Del Riesgo'),
        ('Mercadeo', 'Mercadeo'),
        ('Transversal', 'Transversal'),
    ]

    title = models.CharField(max_length=200, verbose_name='Nombre del Bug')
    reported_by = models.CharField(max_length=100, verbose_name='Reportado por')
    date_reported = models.DateField(verbose_name='Fecha de Creación')
    area = models.CharField(max_length=100, verbose_name='Área', choices=AREA_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Estado')
    project_name = models.CharField(max_length=100, verbose_name='Nombre del Proyecto')
    causal = models.CharField(max_length=50, choices=CAUSAL_CHOICES)
    link = models.URLField(max_length=200, verbose_name='Enlace')
    assigned_to = models.CharField(max_length=100, verbose_name='Encargado')
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, verbose_name='Severidad')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Reportes de Bugs"
