from django.forms import *
from .models import Incidencia

class IncidenciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'


    class Meta:
        model = Incidencia
        fields = '__all__'
        exclude = ['fecha_creado']
        widgets = {
            'titulo': TextInput(
                attrs={
                    'placeholder': 'Titulo de Incidencia',
                    'autofocus': True
                }
            ),
            'cliente': TextInput(
                attrs={
                    'placeholder': 'Nombre del cliente'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Descripción de la Incidencia',
                    'rows': 4,
                    'cols': 4
                }
            ),
            'respuesta': Textarea(
                attrs={
                    'placeholder': 'Aún no presenta respuesta',
                    'rows': 3,
                    'cols': 3
                }
            )
        }

class respuestaForm(Form):
    nivelR = CharField(required=False, widget=Select(attrs={
        'class': 'form-control',
    }, choices=[
        ('1', '1'), 
        ('2', '2'), 
        ('Proveedor', 'Proveedor')
    ]))
    prioridadR = CharField( required=False, widget=Select(attrs={
        'class': 'form-control',
    }, choices=[
        ('Baja', 'Baja'), 
        ('Media', 'Media'), 
        ('Alta', 'Alta')
    ]))
    respuestaR = CharField(required=False, widget=Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Aún no presenta respuesta',
        'rows': 3,
        'cols': 3
    }))

class ReporteFechaForm(Form):
    date_range = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))
    
class ReporteFechaForm2(Form):
    fecha_inicio = DateField(input_formats='%Y-%m-%d',widget=DateInput(
        format= '%Y-%m-%d',
        attrs={
            'type': 'date',
            'placeholder': 'Año-Mes-Día',
            'class': 'form-control',
            'autcomplete': 'off'
        }
    ))
    fecha_fin = DateField(input_formats='%Y-%m-%d',widget=DateInput(
        format= '%Y-%m-%d',
        attrs={
            'type': 'date',
            'placeholder': 'Año-Mes-Día',
            'class': 'form-control',
            'autcomplete': 'off'
        }
    ))