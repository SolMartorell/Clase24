from django.forms import Form, IntegerField, CharField, EmailField, DateField, BooleanField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(Form):

    nombre = CharField()
    camada = IntegerField()


class ProfesorFormulario(Form):

    nombre = CharField()
    apellido = CharField()
    email = EmailField()
    profesion = CharField()


class EstudianteFormulario(Form):

    nombre = CharField()
    apellido = CharField()
    email = EmailField()


class EntregableFormulario(Form):
    nombre = CharField()
    fecha_entrega = DateField()
    entregado = BooleanField()



class UserCustomCreationForm(UserCreationForm):

    email = EmailField()
    password1 = CharField(label="Contraseña", widget=PasswordInput)
    password2 = CharField(label="Confirmar contraseña", widget=PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = { "username": "", "email": "", "password1": "", "password2": "" }


class UserEditForm(UserCreationForm):

    first_name = CharField(label="Nombre")
    last_name = CharField(label="Apellido")
    email = EmailField(label="Ingrese un email nuevo")
    password1 = CharField(label="Contraseña nueva", widget=PasswordInput)
    password2 = CharField(label="Confirmar contraseña nueva", widget=PasswordInput)
   
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]
        help_texts = {"first_name": "", "last_name": "", "email": "", "password1": "", "password2": ""}


class AvatarForm(Form):
    imagen = ImageField() 