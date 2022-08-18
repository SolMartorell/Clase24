from django.contrib import admin
from coder.models import Avatar, Curso, Entregable, Profesor, Estudiante

# Register your models here.

admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Avatar)