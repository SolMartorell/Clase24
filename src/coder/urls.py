from django.urls import path
from coder.views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name="inicio"),
    
    path("cursos/", cursos, name='cursos'),
    path("cursos/borrar/<id_curso>", borrar_curso, name="borrar_curso"),
    path("cursos/editar/<id_curso>", actualizar_curso, name="editar_curso"),
    
    
    path("estudiantes/", estudiante, name='estudiantes'),

    path("entregables/", entregable, name='entregables'),
    
    path("formulario/", formulario_busqueda, name="FormularioBusqueda"),
    path("resultados/", buscar, name="buscar_curso"),
    
    path("profesores/", ProfesoresList.as_view(), name='profesores'),
    path("profesores/crear", ProfesorCreate.as_view(), name="profesor_create"),
    path("profesores/actualizar/<pk>", ProfesorUpdate.as_view(), name="profesor_update"),
    path("profesores/borrar/<pk>", ProfesorDelete.as_view(), name="profesor_delete"),
    path("profesores/<pk>", ProfesorDetail.as_view(), name="profesor_detail"),

    path("login/", iniciar_sesion, name="iniciar_sesion"),
    path("register/", registrar_usuario, name="registro"),
    path("logout/", LogoutView.as_view(template_name="coder/logout.html"), name="logout"),
    path("edit/", editar_usuario, name="editar_usuario"),
    path("avatar/", agregar_avatar, name="agregar_avatar")
]
