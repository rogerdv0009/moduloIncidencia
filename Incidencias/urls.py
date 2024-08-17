from django.urls import path
from Incidencias import views
urlpatterns = [
    path('login/', views.usuarioFormView.as_view(), name='Login'),
    path('logout/', views.usuarioLogoutView.as_view(), name='Logout'),
    path('principal/', views.principalListView.as_view(), name='Principal'),
    # path('principalEE/', views.principalListViewEnEspera.as_view(), name='PrincipalEnEspera'),
    # path('principalC/', views.principalListViewCerradas.as_view(), name='PrincipalCerradas'),
    # path('principalPC/', views.principalListViewPendienteC.as_view(), name='PrincipalPendienteC'),
    # path('principalPR/', views.principalListViewPendienteR.as_view(), name='PrincipalPendienteR'),
    path('procesarI/<int:pk>/', views.procesarIncidencia.as_view(), name='ProcesarI'),
    # path('base/', views.baseListView.as_view(), name='BaseConocimiento'),
    # path('insertarB/', views.baseCreateView.as_view(), name='InsertarB'),
    # path('editarB/<int:pk>/', views.baseUpdateView.as_view(), name='EditarB'),
    # path('eliminarB/<int:pk>/', views.baseDeleteView.as_view(), name='EliminarB'),
    # path('verB/<int:pk>/', views.baseDetailView.as_view(), name='VerB'),
    path('acerca/', views.AcercaDe, name='AcercaDe'),
    path('insertarI/', views.incidenciaCreateView.as_view(), name='InsertarI'),
    path('editarI/<int:pk>/', views.incidenciaUpdateView.as_view(), name='EditarI'),
    path('eliminarI/<int:pk>/', views.incidenciaDeleteView.as_view(), name='EliminarI'),
    path('verI/<int:pk>/', views.incidenciaDetailView.as_view(), name='VerI'),
    path('reporte_I/', views.reporte_Incidencia.as_view(), name='Reporte_I'),
    path('reporteI/<str:fecha_i>/<str:fecha_f>/', views.reportesIncidencia.as_view(), name='ReporteI'),
]