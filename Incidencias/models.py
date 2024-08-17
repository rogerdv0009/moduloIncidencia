from django.db import models
from django.forms import model_to_dict
from  user.models import User
from datetime import datetime
# Create your models here.

# Aquí se muestran las opciones para cada uno de los select de las incidencias
incidencia_sistema = [
    (1, 'CIDI'),
    (2, 'CESOL'),
    (3, 'VERTEX'),
    (4, 'CESIM'),
    (5, 'XETID'),
    (6, 'OTRA')
]

incidencia_entrada = [
    (1, 'Llamada'),
    (2, 'Correo')
]

incidencia_estado = [
    (1, 'En Espera'),
    (2, 'Cerrada'),
    (3, 'Pendiente Recordatorio'),
    (4, 'Pendiente Cerrar')
]

incidencia_nivel = [
    (1, '1'),
    (2, '2'),
    (3, 'Proveedor')
]

incidencia_prioridad = [
    (1, 'Baja'),
    (2, 'Media'),
    (3, 'Alta')
]

incidencia_grupo = [
    (1, 'Especialistas de Desarrollo'),
    (2, 'Etecsa'),
    (3, 'Soporte Técnico')
]

incidencia_organizacion = [
    (1, 'AGR'),
    (2, 'AIN'),
    (3, 'ANPP'),
    (4, 'BanMet'),
    (5, 'BCC'),
    (6, 'CAP-Camaguey'),
    (7, 'CAP-Granma'),
    (8, 'CAP-Guantánamo'),
    (9, 'CAP-La Habana'),
    (10, 'CAP-Las Tunas'),
    (11, 'CAP-Matanzas'),
    (12, 'CAP-Mayabeque'),
    (13, 'CAP-Pinar del Río'),
    (14, 'CCOIFP'),
    (15, 'CCPCC'),
    (16, 'CEDESA'),
    (17, 'CEJ'),
    (18, 'Centro Soporte'),
]

# class Base_Conocimiento(models.Model):
#     nombreSistema = models.IntegerField(
#         null = False, blank = False,
#         choices = incidencia_sistema,
#         default = 1
#     )
#     nombreProyecto = models.CharField(max_length=150, verbose_name='Proyecto')
#     IncidenciasA = models.CharField(max_length=500, verbose_name='Incidencias', default='Incidencia')
#     manual = models.FileField(upload_to='manuales/%y/%m/%d', default='No contiene')
#     respuestasAnexadas = models.TextField(verbose_name='Respuestas')
#     fecha_creado_base = models.DateTimeField(auto_now_add=True, null=True, blank=True)

        
#     class Meta:
#         ordering= ['-id']
        
#     def __str__(self):
#         return self.nombreProyecto
    
#     def ObtenerSistema(self):
#         sistema = self.nombreSistema
#         if sistema == 1:
#             nombre = "CIDI"
#         elif sistema == 2:
#             nombre = "CESOL"
#         elif sistema == 3:
#             nombre = "VERTEX"
#         elif sistema == 4:
#             nombre = "CESIM"
#         elif sistema == 5:
#             nombre = "XETID"
#         elif sistema == 6:
#             nombre = "OTRA"
#         return str(nombre)

    
# Clase Incidencia con sus respectivos parámetros

class Incidencia(models.Model):
    titulo = models.CharField(max_length=100)
    cliente = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500, verbose_name="Descripción")
    entrada = models.IntegerField(
        null = False, blank = False,
        choices = incidencia_entrada,
        default = 1
    )
    #BaseA = models.ForeignKey(Base_Conocimiento, on_delete=models.CASCADE, null = True, blank=True, verbose_name="BDC Anexada")
    estado = models.IntegerField(
        null = False, blank = False,
        choices = incidencia_estado,
        default = 1
    )
    nivel = models.IntegerField(
        null = True, blank = True,
        choices = incidencia_nivel,
        default = 1
    )
    prioridad = models.IntegerField(
        null = True, blank = True,
        choices = incidencia_prioridad,
        default = 2
    )
    sistema = models.IntegerField(
        null = False, blank = False,
        choices = incidencia_sistema,
        default = 1,
        verbose_name="Centro de Desarrollo"
    )
    grupo = models.IntegerField(
        null = False, blank = False,
        choices = incidencia_grupo,
        default = 1
    )
    organizacion = models.IntegerField(
        verbose_name="Organización",
        null = False, blank = False,
        choices = incidencia_organizacion,
        default = 1
    )
    responsable = models.ForeignKey(User, on_delete=models.CASCADE, null = True, verbose_name="Responsable")
    respuesta = models.TextField(verbose_name='Respuesta', blank=True, null=True, max_length=500)
    fecha_creado = models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering= ['-id']
    
    def ObtenerNivel(self):
        nivel = self.nivel
        if nivel == 1:
            nom = "1"
        elif nivel == 2:
            nom = "2"
        elif nivel == 3:
            nom = "Proveedor"
        return str(nom)
    
    def ObtenerGrupo(self):
        grupo = self.grupo
        if grupo == 1:
            nom = "Especialistas de Desarrollo"
        elif grupo == 2:
            nom = "Etecsa"
        elif grupo == 3:
            nom = "Soporte Técnico"
        return str(nom)
    
    def ObtenerOrganizacion(self):
        organizaciones = self.organizacion
        if organizaciones == 1:
            nom = "AGR"
        elif organizaciones == 2:
            nom = "AIN"
        elif organizaciones == 3:
            nom = "ANPP"
        elif organizaciones == 4:
            nom = "BanMet"
        elif organizaciones == 5:
            nom = "BCC"
        elif organizaciones == 6:
            nom = "CAP-Camaguey"
        elif organizaciones == 7:
            nom = "CAP-Granma"
        elif organizaciones == 8:
            nom = "CAP-Guantánamo"
        elif organizaciones == 9:
            nom = "CAP-La Habana"
        elif organizaciones == 10:
            nom = "CAP-Las Tunas"
        elif organizaciones == 11:
            nom = "CAP-Matanzas"
        elif organizaciones == 12:
            nom = "CAP-Mayabeque"
        elif organizaciones == 13:
            nom = "CAP-Pinar del Río"
        elif organizaciones == 14:
            nom = "CCOIFP"
        elif organizaciones == 15:
            nom = "CCPCC"
        elif organizaciones == 16:
            nom = "CEDESA"
        elif organizaciones == 17:
            nom = "CEJ"
        elif organizaciones == 18:
            nom = "Centro Soporte"
        return str(nom)

    def ObtenerEstado(self):
        state = self.estado
        if state == 1:
            nombre = "En Espera"
        elif state == 2:
            nombre = "Cerrada"
        elif state == 3:
            nombre = "Pendiente Recordatorio"
        elif state == 4:
            nombre = "Pendiente Cerrar"
        return str(nombre)

    def ObtenerPrioridad(self):
        priority = self.prioridad
        if priority == 1:
            nombre = "Baja"
        elif priority == 2:
            nombre = "Media"
        elif priority == 3:
            nombre = "Alta"
        return str(nombre)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
        