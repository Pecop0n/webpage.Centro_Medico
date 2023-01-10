from django.shortcuts import render, redirect, HttpResponse
from .models import HorasMedicas, Pacientes
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, login

# Create your views here.

##### CRUD PART 1 ###
def login(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("Usuario o Contrasela es incorrectas!")


    return render(request, "login.html")

def loginMedico(request):
    return render(request, "loginMedico.html")

def usuarios(request):
    return render(request, "usuarios.html")

def index(request):
    return render(request, "index.html")

def horasMedicas(request):
    horaslistado = HorasMedicas.objects.all()
    messages.success(request, 'Bienvenido!')
    return render(request, "horasMedicas.html", {"horasmedicas": horaslistado })

def home(request):
    pacientesListado = Pacientes.objects.all()
    messages.success(request, 'Bienvenido!')
    return render(request, "gestionPacientes.html", {"paciente": pacientesListado })

def registrarPaciente(request):
    txtNombre_pa = request.POST['txtNombre_pa']
    txtApellido_pa = request.POST['txtApellido_pa']
    txtRUT_pa = request.POST['txtRUT_pa']
    numbEdad_pa = request.POST['numbEdad_pa']
    txtSexo_pa = request.POST['txtSexo_pa']
    txtSeguro_pa = request.POST['txtSeguro_pa']
    dteFechaIngres_pa = request.POST['dteFechaIngres_pa']

    paciente = Pacientes.objects.create(
        pa_nombre=txtNombre_pa, pa_apellido= txtApellido_pa, pa_rut=txtRUT_pa, pa_edad=numbEdad_pa, 
        sexo=txtSexo_pa, seguro=txtSeguro_pa, fec_ingreso= dteFechaIngres_pa)
    messages.success(request, 'Pacientes Registrado')
    return redirect('GestionPaciente')

def edicionPacientes(request, id_paciente):
    paciente = Pacientes.objects.get(id_paciente=id_paciente)
    return render(request, "edicionPacientes.html", {"paciente": paciente})

def editarPaciente(request):
    numbID_paciente = request.POST['numbID_paciente']
    txtNombre_pa = request.POST['txtNombre_pa']
    txtApellido_pa = request.POST['txtApellido_pa']
    txtRUT_pa = request.POST['txtRUT_pa']
    numbEdad_pa = request.POST['numbEdad_pa']
    txtSexo_pa = request.POST['txtSexo_pa']
    txtSeguro_pa = request.POST['txtSeguro_pa']
    dteFechaIngres_pa = request.POST['dteFechaIngres_pa']

    """ paciente = Pacientes.objects.get(id_paciente=numbID_paciente)
    paciente.numbID_paciente = numbID_paciente
    paciente.txtNombre_pa = txtNombre_pa
    paciente.txtApellido_pa = txtApellido_pa
    paciente.txtRUT_pa = txtRUT_pa
    paciente.numbEdad_pa = numbEdad_pa
    paciente.txtSexo_pa = txtSexo_pa
    paciente.txtSeguro_pa = txtSeguro_pa
    paciente.dteFechaIngres_pa = dteFechaIngres_pa
    paciente.save() """

    Pacientes.objects.filter(id_paciente = numbID_paciente).update(id_paciente = numbID_paciente, pa_nombre = txtNombre_pa, pa_apellido = txtApellido_pa,
    pa_rut = txtRUT_pa, pa_edad = numbEdad_pa, sexo = txtSexo_pa, seguro = txtSeguro_pa,
    fec_ingreso = dteFechaIngres_pa)

    messages.success(request, 'La informacion del paciente a sido actulizada')

    return redirect('GestionPaciente')


def eliminarPacientes(request, id_paciente):
    paciente = Pacientes.objects.get(id_paciente=id_paciente)
    paciente.delete()

    messages.success(request, 'El paciente a fue eliminado')

    
    return redirect('GestionPaciente')

##### FIN CRUD PART 1###

##### CRUD PART 2###

def registrarHoraMedica(request):
    txtPaciente = request.POST['txtPaciente']
    txtMedico = request.POST['txtMedico']
    txtConsulta = request.POST['txtConsulta']
    dteFecConsulta = request.POST['dteFecConsulta']
    correo = request.POST['correo']
    txtEstado_pa = request.POST['txtEstado_pa']

    HorasMedicas(paciente = txtPaciente, medico = txtMedico, consulta = txtConsulta, fec_consulta = dteFecConsulta, estado = txtEstado_pa).save()
    EnviarCorreo(txtPaciente, txtMedico, txtConsulta, dteFecConsulta, correo, txtEstado_pa)
    messages.success(request, 'Hora Registrada')
    return redirect('HorasMedicas')

def EnviarCorreo(txtPaciente, txtMedico, txtConsulta, dteFecConsulta, correo, txtEstado_pa):
    context = {'txtPaciente' : txtPaciente, 'txtMedico' : txtMedico, 'txtConsulta' : txtConsulta, 'dteFecConsulta' : dteFecConsulta,
    'correo' : correo, 'txtEstado_pa' : txtEstado_pa}
    template = get_template('correoConfirmacion.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Correo Confirmacion Hora',
        'Centro Medico Galenos',
        settings.EMAIL_HOST_USER,
        [correo]
    )
    email.attach_alternative(content, 'text/html')
    email.send()

def edicionHoramedica(request, id_horamedica):
    horamedica = HorasMedicas.objects.get(id_horamedica=id_horamedica)
    return render(request, "edicionHorasMedicas.html", {"horamedica": horamedica})

def editarHoramedica(request):
    numbID_horamedica = request.POST['numbID_paciente']
    txtPaciente = request.POST['txtPaciente']
    txtMedico = request.POST['txtMedico']
    txtConsulta = request.POST['txtConsulta']
    dteFecConsulta = request.POST['dteFecConsulta']
    txtEstado_pa = request.POST['txtEstado_pa']

    """ horamedica = HorasMedicas.objects.get(id_horamedica=numbID_horamedica)
    horamedica.numbID_paciente = txtPaciente
    horamedica.txtPaciente = txtMedico
    horamedica.txtConsulta = txtConsulta
    horamedica.dteFecConsulta = dteFecConsulta
    horamedica.txtEstado_pa = txtEstado_pa
    horamedica.save() """

    HorasMedicas.objects.filter(id_horamedica = numbID_horamedica).update(consulta = txtConsulta,
    fec_consulta = dteFecConsulta, estado = txtEstado_pa)

    messages.success(request, 'La Hora medica a sido modificada!')

    return redirect('HorasMedicas')


def eliminarHoramedica(request, id_horamedica):
    horamedica = HorasMedicas.objects.get(id_horamedica=id_horamedica)
    horamedica.delete()

    messages.success(request, 'El paciente a sido atendido!')

    
    return redirect('HorasMedicas')

##### FIN CRUD PART 2###

##### CRUD PART 3###
def atencionPacientes(request):
    atencionPacientes = HorasMedicas.objects.all()
    messages.success(request, 'Bienvenido!')
    return render(request, "atencionPacientes.html", {"atencionPacientes": atencionPacientes })

def eliminarAtencion(request, id_horamedica):
    atencionPacientes = HorasMedicas.objects.get(id_horamedica=id_horamedica)
    atencionPacientes.delete()

    messages.success(request, 'El paciente a sido atendido!')

    return redirect('AtencionPacientes')
