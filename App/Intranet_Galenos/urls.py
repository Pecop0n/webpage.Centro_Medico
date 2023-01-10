from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.usuarios, name = 'vistaUsuario'),
    path('index', views.index, name = 'index'),

    path('login', views.login, name= 'login'),
    path('loginMedico', views.loginMedico, name= 'loginMedico'),

    path('gestionPacientes/', views.home, name= 'GestionPaciente'),
    path('registrarPaciente/', views.registrarPaciente),

    path('edicionPacientes/<id_paciente>', views.edicionPacientes, name = 'EdicionPacientes'),
    path('editarPaciente/', views.editarPaciente, name = 'EditarPaciente'),
    path('eliminarPacientes/<id_paciente>', views.eliminarPacientes, name = 'EliminarPaciente'),

    path('horasMedicas/', views.horasMedicas, name='HorasMedicas'),
    path('registrarHoraMedica/', views.registrarHoraMedica),
    path('edicionHoramedica/<id_horamedica>', views.edicionHoramedica, name = 'EdicionHoraMedica'),

    path('editarHoramedica/', views.editarHoramedica, name = 'EditarHoraMedica'),
    path('eliminarHoramedica/<id_horamedica>', views.eliminarHoramedica, name = 'EliminarHoraMedica'),

    path('atencionPacientes/', views.atencionPacientes, name='AtencionPacientes'),
    path('eliminarAtencion/<id_horamedica>', views.eliminarAtencion, name = 'EliminarAtencion'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
