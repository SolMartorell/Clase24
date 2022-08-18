
from django.shortcuts import render, redirect
from django.http import HttpResponse
from coder.models import Curso, Estudiante, Profesor, Entregable, Avatar
from coder.forms import CursoFormulario, UserCustomCreationForm, UserEditForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def inicio(request):

    avatar = Avatar.objects.filter(usuario=request.user).first()

    context = {
        "mensaje": "La comision 40150 es la mejor!",
        "mensaje_bienvenida": "Bienvenid@s!",
        "imagen": avatar.imagen.url
    }

    return render(request, "coder/index.html", context)


def estudiante(request):
    return HttpResponse("Vista de estudiante")



def entregable(request):
    return HttpResponse("Vista de entregable")

@login_required
def cursos(request):

    cursos = Curso.objects.all()

    if request.method == "GET":
        formulario = CursoFormulario()

    
        context = {
            "mensaje": "Todos nuestros cursos al mejor precio!",
            "mensaje_bienvenida": "Bienvenid@s!",
            "cursos": cursos,
            "formulario": formulario
        }

        return render(request, "coder/cursos.html", context)

    else:
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():        
            data = formulario.cleaned_data

            nombre = data.get("nombre")
            camada = data.get("camada")
            curso = Curso(nombre=nombre, camada=camada)

            curso.save()

        formulario = CursoFormulario()
        context = {
            "mensaje": "Todos nuestros cursos al mejor precio!",
            "mensaje_bienvenida": "Bienvenid@s!",
            "cursos": cursos,
            "formulario": formulario
        }

        return render(request, "coder/cursos.html", context)



def borrar_curso(request, id_curso):
    try:
        curso = Curso.objects.get(id=id_curso)
        curso.delete()
        return redirect("cursos")
    except:
        return redirect("inicio")




def actualizar_curso(request, id_curso):

    if request.method == "GET":
        formulario = CursoFormulario()
        contexto = {
            "formulario": formulario
        }

        return render(request, "coder/cursos_actualizar.html", contexto)
    
    else:
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            try:
                curso = Curso.objects.get(id=id_curso)

                curso.nombre = data.get("nombre")
                curso.camada = data.get("camada")
                curso.save()
            except:
                return HttpResponse("Error en la actualizacion")
        

        return redirect("cursos")

















def formulario_busqueda(request):
    return render(request, "coder/formulario_busqueda.html")

def buscar(request):

    curso_nombre = request.GET.get("curso", None)
    camada = request.GET.get("camada", None)

    if not curso_nombre:
        return HttpResponse("No indicaste ningun nombre")

    cursos_lista = Curso.objects.filter(nombre__icontains=curso_nombre)

    if camada:
        cursos_lista = cursos_lista.filter(camada=camada)
    return render(request, "coder/resultado_busqueda.html", {"cursos": cursos_lista})











class ProfesoresList(ListView):
    model = Profesor
    template_name = "coder/profesores_list.html"


class ProfesorDetail(DetailView):
    model = Profesor
    template_name = "coder/profesor_detail.html"



class ProfesorCreate(LoginRequiredMixin, CreateView):
    model = Profesor
    success_url = "/coder/profesores/"
    fields = ["nombre", "apellido", "email", "profesion"]

class ProfesorUpdate(LoginRequiredMixin, UpdateView):
    model = Profesor
    success_url = "/coder/profesores/"
    fields = ["nombre", "apellido", "email", "profesion"]

class ProfesorDelete(LoginRequiredMixin, DeleteView):
    model = Profesor
    success_url = "/coder/profesores/"






def iniciar_sesion(request):
    if request.method == "GET":
        formulario = AuthenticationForm()

        context = {
            "form": formulario
        }

        return render(request, "coder/login.html", context)

    else:
        formulario  = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = authenticate(username=data.get("username"), password=data.get("password"))

            if usuario is not None:
                login(request, usuario)
                return redirect("inicio")
            else:
                context = {
                    "error": "Credenciales no validas",
                    "form": formulario
                }
                return render(request, "coder/login.html", context)
        else:
            context = {
                "error": "Formulario NO valido",
                "form": formulario
            }
            return render(request, "coder/login.html", context)



def registrar_usuario(request):
    if request.method == "GET":
        formulario = UserCustomCreationForm()
        return render(request, "coder/registro.html", {"form": formulario})
    else:
        formulario = UserCustomCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        else:
            return render(request, "coder/registro.html", {"form": formulario, "error": "Formulario NO valido"})


@login_required
def editar_usuario(request):
    
    if request.method == "GET":
        form = UserEditForm(initial={"email": request.user.email, "first_name": request.user.first_name, "last_name": request.user.last_name})
        return render(request, "coder/update_user.html", {"form": form})
    else:
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            usuario = request.user

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]

            usuario.save()

            return redirect("inicio")

        else:
            return render(request, "coder/update_user.html", {"form": form})



@login_required
def agregar_avatar(request):
    
    if request.method == "GET":
       form = AvatarForm()
       return render(request, "coder/agregar_avatar.html", {"form": form})
    else:
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
                data = form.cleaned_data
                
                usuario = User.objects.filter(username=request.user.username).first()
                avatar = Avatar(usuario=usuario, imagen=data["imagen"])
                
                return redirect("inicio")

        else:
            return render(request, "coder/agregar_avatar.html", {"form": form})