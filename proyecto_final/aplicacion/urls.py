from django.urls import path
from .views import IniciarSesion, ProgramarCita, TurnosDados, CancelarCita, EditarCita

urlpatterns = [
    path("internauta/login", IniciarSesion, name="login"),
    path("Secretaria/programar_cita", ProgramarCita, name="programar_cita"),
    path("Secretaria/turnos_dados", TurnosDados, name="turnos_dados"),
    path("Secretaria/cancelar_cita/<int:cita>", CancelarCita, name="cancelar_cita"),
    path("Secretaria/editar_cita/<int:cita>", EditarCita, name="editar_cita"),
]
