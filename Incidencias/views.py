from datetime import datetime
from typing import Any
from django import http
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.query import QuerySet
from CentroSoporte.settings import MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL
from .forms import IncidenciaForm, ReporteFechaForm, respuestaForm
from .models import Incidencia
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, DetailView, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import os
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.shortcuts import HttpResponseRedirect, render
# Create your views here.

startDate = ''
endDate = ''
class principalListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = '/incidencias/login/'
    permission_required = ('Incidencias.add_incidencia')
    model = Incidencia
    template_name = "Principal.html"

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     contexto = super().get_context_data(**kwargs)
    #     contexto['incidencias'] = Incidencia.objects.all()
    #     return contexto
    
    def get_queryset(self):
        queryset = super().get_queryset()
        valor_select = self.request.GET.get('Filtrado_Estados')
        if valor_select:
            if valor_select == '0':
                return queryset
            elif valor_select == '1':
                number = int(1)
                queryset = queryset.filter(estado = number)
            elif valor_select == '2':
                number = int(2)
                queryset = queryset.filter(estado = number)
            elif valor_select == '3':
                number = int(3)
                queryset = queryset.filter(estado = number)
            elif valor_select == '4':
                number = int(4)
                queryset = queryset.filter(estado = number)
        return queryset
    
    
# class principalListViewEnEspera(LoginRequiredMixin, PermissionRequiredMixin, ListView):
#     login_url = '/incidencias/login/'
#     permission_required = ('Incidencias.add_incidencia')
#     model = Incidencia
#     template_name = "PrincipalEnEspera.html"

#     def EnEspera(): 
#         modelo = Incidencia.objects.all()                       # 1
#         cerradas = 0                                            # 2 
#         for m in modelo:                                        # 3
#             if m.ObtenerEstado() == 'En Espera':                # 4
#                 cerradas = cerradas + 1                         # 5
#         return cerradas                                         # F
    
#     # @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

    
#     def get_context_data(self, **kwargs):
#         contexto = super().get_context_data(**kwargs)
#         contexto['incidencias'] = Incidencia.objects.all()
#         contexto['estado'] = self.EnEspera
#         return contexto


# class principalListViewCerradas(LoginRequiredMixin, PermissionRequiredMixin, ListView):
#     login_url = '/incidencias/login/'
#     permission_required = ('Incidencias.add_incidencia')
#     model = Incidencia
#     template_name = "PrincipalCerradas.html"

#     def EsCerrada():
#         modelo = Incidencia.objects.all()
#         cerradas = 0
#         for m in modelo:
#             if m.ObtenerEstado() == 'Cerrada':
#                 cerradas = cerradas + 1
#         return cerradas
    
#     # @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         contexto = super().get_context_data(**kwargs)
#         contexto['incidencias'] = Incidencia.objects.all()
#         contexto['estado'] = self.EsCerrada
#         return contexto


# class principalListViewPendienteC(LoginRequiredMixin, PermissionRequiredMixin, ListView):
#     login_url = '/incidencias/login/'
#     permission_required = ('Incidencias.add_incidencia')
#     model = Incidencia
#     template_name = "PrincipalPendienteC.html"

#     def PendienteC():
#         modelo = Incidencia.objects.all()
#         cerradas = 0
#         for m in modelo:
#             if m.ObtenerEstado() == 'Pendiente Cerrar':
#                 cerradas = cerradas + 1
#         return cerradas
    
#     # @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         contexto = super().get_context_data(**kwargs)
#         contexto['incidencias'] = Incidencia.objects.all()
#         contexto['estado'] = self.PendienteC
#         return contexto


# class principalListViewPendienteR(LoginRequiredMixin, PermissionRequiredMixin, ListView):
#     login_url = '/incidencias/login/'
#     permission_required = ('Incidencias.add_incidencia')
#     model = Incidencia
#     template_name = "PrincipalPendienteR.html"

#     def PendienteR():
#         modelo = Incidencia.objects.all()
#         cerradas = 0
#         for m in modelo:
#             if m.ObtenerEstado() == 'Pendiente Recordatorio':
#                 cerradas = cerradas + 1
#         return cerradas

#     # @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         contexto = super().get_context_data(**kwargs)
#         contexto['incidencias'] = Incidencia.objects.all()
#         contexto['estado'] = self.PendienteR
#         return contexto


class incidenciaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = '/incidencias/login/'
    permission_required = ('Incidencias.add_incidencia',
                           'Incidencias.change_incidencia')
    model = Incidencia
    form_class = IncidenciaForm
    template_name = "Insertar_Incidencia.html"
    success_url = reverse_lazy('Principal')

    # @method_decorator(login_required)
    #@method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class incidenciaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/incidencias/login/'
    permission_required = ('Incidencias.add_incidencia',
                           'Incidencias.change_incidencia')
    model = Incidencia
    form_class = IncidenciaForm
    template_name = "Editar_Incidencia.html"
    success_url = reverse_lazy('Principal')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class procesarIncidencia(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/incidencias/login/'
    permission_required = ('Incidencias.add_incidencia',
                           'Incidencias.change_incidencia')
    model = Incidencia
    form_class = IncidenciaForm
    template_name = "ProcesarI.html"
    success_url = reverse_lazy('Principal')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        incidencia_respuesta = Incidencia.objects.get(pk=self.kwargs['pk'])
        primaryKey = incidencia_respuesta.pk
        titulo_incidencia = incidencia_respuesta.titulo
        descripcion_incidencia = incidencia_respuesta.descripcion
        incidencias_cerradas = Incidencia.objects.filter(estado__exact=2)
        incidencias_filtradas = incidencias_cerradas.filter(descripcion__icontains=descripcion_incidencia)
        mismo_titulo = incidencias_cerradas.filter(titulo__icontains=titulo_incidencia)
        contexto = {
            'form': self.form_class,
            'primaryKey': primaryKey,
            'incidencias_filtradas': incidencias_filtradas,
            'mismo_titulo': mismo_titulo
        }
        return self.render_to_response(contexto)

class incidenciaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = '/incidencias/login/'
    permission_required = ('Incidencias.add_incidencia',
                           'Incidencias.change_incidencia', 'Incidencias.delete_incidencia')
    model = Incidencia
    template_name = 'Eliminar_Incidencia.html'
    success_url = reverse_lazy('Principal')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class incidenciaFormView(LoginRequiredMixin, FormView):
    login_url = '/incidencias/login/'
    form_class = IncidenciaForm
    template_name = "Insertar_Incidencia.html"
    success_url = reverse_lazy('Principal')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class incidenciaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = '/incidencias/login/'
    permission_required = ('Incidencias.view_incidencia')
    model = Incidencia
    template_name = "Ver_Incidencia.html"


#Vistas para los reportes, la exportacion a pdf y los graficos

class reporte_Incidencia(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model= Incidencia
    form_class= IncidenciaForm
    template_name = "reporte_Incidencias.html" 
    login_url = '/incidencias/login/'
    permission_required = ('Incidencias.add_incidencia',
                           'Incidencias.change_incidencia', 'Incidencias.delete_incidencia')
    fecha_i = ''
    fecha_f = ''
    @method_decorator(csrf_exempt)  
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action =='report_data':
                data = []
                startDate = request.POST.get('start_date','')
                endDate = request.POST.get('end_date','')
                search = Incidencia.objects.all()
                if len(startDate) and len(endDate):
                    search = search.filter(fecha_creado__range=(startDate, endDate))
                    self.fecha_i = startDate
                    self.fecha_f = endDate
                for s in search:
                    data.append([
                        s.pk,
                        s.cliente,
                        s.ObtenerEstado(),
                        s.fecha_creado.strftime('%Y-%m-%d'),
                        s.ObtenerNivel(),
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha_i'] = self.fecha_i
        context['fecha_f'] = self.fecha_f
        context["formulario"] = ReporteFechaForm()
        return context
    


class reportesIncidencia(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    login_url = '/incidencias/login/'
    permission_required = ('Incidencias.view_incidencia', 'Incidencias.change_incidencia',
                           'Incidencias.delete_incidencia', 'Incidencias.add_incidencia')

    def obtenerCantidadEnEspera():
        cont = 0
        incidencias = Incidencia.objects.all()
        for incidencia in incidencias:
            if incidencia.ObtenerEstado() == 'En Espera':
                cont += 1
        return cont

    def obtenerCantidadCerradas():
        cont = 0
        incidencias = Incidencia.objects.all()
        for incidencia in incidencias:
            if incidencia.ObtenerEstado() == 'Cerrada':
                cont += 1
        return cont

    def obtenerCantidadPRecordatorio():
        cont = 0
        incidencias = Incidencia.objects.all()
        for incidencia in incidencias:
            if incidencia.ObtenerEstado() == 'Pendiente Recordatorio':
                cont += 1
        return cont

    def obtenerCantidadPCerrar():
        cont = 0
        incidencias = Incidencia.objects.all()
        for incidencia in incidencias:
            if incidencia.ObtenerEstado() == 'Pendiente Cerrar':
                cont += 1
        return cont

    def obtenerCantidadBaja():
        cont = 0
        incidencias = Incidencia.objects.all()
        for incidencia in incidencias:
            if incidencia.prioridad == 1:
                cont += 1
        return cont

    def obtenerCantidadMedia():
        cont = 0
        incidencias = Incidencia.objects.all()
        for incidencia in incidencias:
            if incidencia.prioridad == 2:
                cont += 1
        return cont

    def obtenerCantidadAlta():
        cont = 0
        incidencias = Incidencia.objects.all()
        for incidencia in incidencias:
            if incidencia.prioridad == 3:
                cont += 1
        return cont

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = STATIC_URL        # Typically /static/
            sRoot = STATIC_ROOT      # Typically /home/userX/project_static/
            mUrl = MEDIA_URL         # Typically /media/
            mRoot = MEDIA_ROOT       # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('incidenciasReportes.html')
            #fecha_i = datetime.strptime(self.kwargs['fecha_i'], '%Y-%m-%d').date()
            #fecha_f = datetime.strptime(self.kwargs['fecha_f'], '%Y-%m-%d').date()
            contexto = {
                'incidencias': Incidencia.objects.all(),
                'titulo': 'Incidencias Tecnológicas de Soporte',
                'imagen1': '{}{}'.format(STATIC_URL, 'img/UCI.png'),
                'fondo': '{}{}'.format(STATIC_URL, 'img/fondopdf.png')
            }
            html = template.render(contexto)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Reporte de Incidencias.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response, link_callback=self.link_callback)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('Principal'))


class reportesIncidenciaPorId(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    login_url = '/incidencias/login/'
    permission_required = ('Incidencias.view_incidencia', 'Incidencias.change_incidencia',
                           'Incidencias.delete_incidencia', 'Incidencias.add_incidencia')

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = STATIC_URL        # Typically /static/
            sRoot = STATIC_ROOT      # Typically /home/userX/project_static/
            mUrl = MEDIA_URL         # Typically /media/
            mRoot = MEDIA_ROOT       # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('incidenciasReportes.html')
            html = template.render({'incidencias': Incidencia.objects.get(pk=self.kwargs['pk']),
                                    'titulo': 'Incidencias Tecnológicas de Soporte'
                                    })
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Reporte de Incidencias.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('Principal'))

# Vistas para el usuario

class usuarioFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('Principal')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)


class usuarioLogoutView(LogoutView):
    next_page = 'Login'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# class posibleRespuestas(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
#     login_url = '/incidencias/login/'
#     permission_required = ('Incidencias.view_incidencia', 'Incidencias.change_incidencia',
#                            'Incidencias.delete_incidencia', 'Incidencias.add_incidencia')
#     template_name = "Posible_Respuesta.html"
    
#     def get(self, request, *args, **kwargs):
#         incidencia_respuesta = Incidencia.objects.get(pk=self.kwargs['pk'])
#         titulo_incidencia = incidencia_respuesta.titulo
#         descripcion_incidencia = incidencia_respuesta.descripcion
#         incidencias_cerradas = Incidencia.objects.filter(estado__exact=2)
#         incidencias_filtradas = incidencias_cerradas.filter(descripcion__contains=descripcion_incidencia)
#         mismo_titulo = incidencias_cerradas.filter(titulo__contains=titulo_incidencia)
#         contexto = {
#             'incidencias_filtradas': incidencias_filtradas,
#             'mismo_titulo': mismo_titulo
#         }
#         return self.render_to_response(contexto)
        
        
    
    
# Vistas para la Base de Conocimientos

# class baseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
#     login_url = '/incidencias/login/'
#     permission_required = ('Incidencias.add_base_conocimiento')
#     model = Base_Conocimiento
#     template_name = "baseConocimiento.html"

#     # @method_decorator(login_required)

    
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         contexto = super().get_context_data(**kwargs)
#         contexto['baseC'] = Base_Conocimiento.objects.all()
#         return contexto


# class baseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#     login_url = '/incidencias/login/'
#     permission_required = ('Incidencias.add_base_conocimiento')
#     model = Base_Conocimiento
#     form_class = BaseForm
#     template_name = "Insertar_Base.html"
#     success_url = reverse_lazy('BaseConocimiento')

#     # @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         contexto = super().get_context_data(**kwargs)
#         contexto['incidencias'] = Incidencia.objects.all()
#         contexto['baseC'] = Base_Conocimiento.objects.all()
#         return contexto


# class baseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
#     login_url = '/incidencias/login/'
#     permission_required = ('Incidencias.add_base_conocimiento',
#                            'Incidencias.change_base_conocimiento')
#     model = Base_Conocimiento
#     form_class = BaseForm
#     template_name = "Insertar_Base.html"
#     success_url = reverse_lazy('BaseConocimiento')

#     # @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         contexto = super().get_context_data(**kwargs)
#         contexto['incidencias'] = Incidencia.objects.all()
#         contexto['baseC'] = Base_Conocimiento.objects.all()
#         return contexto


# class baseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
#     login_url = '/incidencias/login/'
#     permission_required = ('Incidencias.add_base_conocimiento',
#                            'Incidencias.change_base_conocimiento', 'Incidencias.delete_base_conocimiento')
#     model = Base_Conocimiento
#     template_name = 'Eliminar_Base.html'
#     success_url = reverse_lazy('BaseConocimiento')

#     # @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)


# class baseDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
#     login_url = '/incidencias/login/'
#     permission_required = ('Incidencias.view_base_conocimiento')
#     model = Base_Conocimiento
#     template_name = "Ver_Base.html"


def AcercaDe(request):

    return render(request, "acercaDe.html")
