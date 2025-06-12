from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm, PecaForm
from .models import Peca
from django.db import IntegrityError
from django.http import HttpResponse
from django.contrib.auth.models import User



def excluir_peca(request, maquina, peca_id):
    peca = get_object_or_404(Peca, id=peca_id, maquina=maquina)
    peca.delete()
    return redirect('adicionar_peca', maquina=maquina)


@login_required

@user_passes_test(lambda u: u.is_superuser)
def selecionar_maquina(request):
    maquinas = [
        'sares1_perfiladoras_fabrica2',
        'sares2_perfiladoras_fabrica2',
        'omera1_prensas_fabrica2',
        'omera2_prensas_fabrica2',
        'omera3_prensas_fabrica2',
        'omera4_prensas_fabrica2',
        'fagor_prensa_F3',
        'pinturapo3_F2',
        'pinturapo4_F2',
        'pinturaliquidaF3',
        'sares4_perfiladorasF3',
        'sares3_perfiladorasF3',
        'jundiai_perfiladorasF3',
        'Aita_prensa_F3',
        'fagorGabinete_perfiladoras_fabrica2',
        'olmaFH_perfiladoras_fabrica2',
        'cosma_perfiladoras_fabrica2',
        # add maquinas
    ]
    return render(request, 'selecionar_maquina.html', {'maquinas': maquinas})

@user_passes_test(lambda u: u.is_superuser)
def adicionar_peca(request, maquina):
    pecas = Peca.objects.filter(maquina=maquina)

    if request.method == 'POST':
        form = PecaForm(request.POST, request.FILES)
        if form.is_valid():
            nova_peca = form.save(commit=False)
            nova_peca.maquina = maquina
            nova_peca.adicionada_por = request.user  # registra o usuário logado
            try:
                nova_peca.save()
                messages.success(request, 'Peça adicionada com sucesso!')
                return redirect('adicionar_peca', maquina=maquina)
            except IntegrityError:
                messages.error(request, 'Já existe uma peça com esse código!')
        else:
            messages.error(request, 'Erro ao adicionar peça. Verifique os campos.')
    else:
        form = PecaForm()

    return render(request, 'adicionar_peca.html', {
        'form': form,
        'pecas': pecas,
        'maquina': maquina
    })

def criar_superusuario(request):
    if User.objects.filter(is_superuser=True).exists():
        return HttpResponse("Já existe um superusuário criado.")
    else:
        User.objects.create_superuser('admin', 'admin@example.com', 'senha123')
        return HttpResponse("Superusuário criado com sucesso! Usuário: admin / Senha: senha123")

def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso. Agora faça login.')
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'cadastro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pag_inicial')  
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')

@login_required
def pag_inicial(request):
    if request.user.is_superuser:
        return redirect('selecionar_maquina') 
    return render(request, 'pag_inicial.html')

@login_required
def pecas_view(request, categoria):
    pecas = Peca.objects.filter(categoria=categoria)
    return render(request, 'pecas_lista.html', {'pecas': pecas})

def pinturapo3_F2(request):
    maquina_nome = 'pinturapo3_F2'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_2/areas_fabrica_2/pintura_fab_2/maquinas_pintura_F2/pinturapo3_F2.html', context)

def pinturapo4_F2(request):
    maquina_nome = 'pinturapo4_F2'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_2/areas_fabrica_2/pintura_fab_2/maquinas_pintura_F2/pinturapo4_F2.html', context)

def omera1_prensas_fabrica2(request):
    maquina_nome = 'omera1_prensas_fabrica2'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_2/areas_fabrica_2/prensas_fab_2/maquinas_prensa_F2/omera1_prensas_fabrica2.html', context)

def omera2_prensas_fabrica2(request):
    maquina_nome = 'omera2_prensas_fabrica2'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_2/areas_fabrica_2/prensas_fab_2/maquinas_prensa_F2/omera2_prensas_fabrica2.html', context)

def omera3_prensas_fabrica2(request):
    maquina_nome = 'omera3_prensas_fabrica2'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_2/areas_fabrica_2/prensas_fab_2/maquinas_prensa_F2/omera3_prensas_fabrica2.html', context)

def omera4_prensas_fabrica2(request):
    maquina_nome = 'omera4_prensas_fabrica2'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_2/areas_fabrica_2/prensas_fab_2/maquinas_prensa_F2/omera4_prensas_fabrica2.html', context)

def peças(request):
    return render(request, 'peças.html')

def escolher_maquina(request):
    return render(request, 'selecionar_maquina.html')

def fabrica2(request):
    return render(request, 'fabrica_2/fabrica2.html')

def prensas_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/prensas_fab_2/prensas_fabrica2.html')

def perfiladora_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2//perfiladora_fabrica2.html')

def cosma_perfiladoras_fabrica2(request):
    maquina_nome = 'cosma_perfiladoras_fabrica2'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2/maquinas_perfiladoras_F2/cosma_perfiladoras_fabrica2.html', context)

def sares1_perfiladoras_fabrica2(request):
    maquina_nome = 'sares1_perfiladoras_fabrica2'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2/maquinas_perfiladoras_F2/sares1_perfiladoras_fabrica2.html', context)

def olmaFH_perfiladoras_fabrica2(request):
    maquina_nome = 'olmaFH_perfiladoras_fabrica2'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2/maquinas_perfiladoras_F2/olmaFH_perfiladoras_fabrica2.html', context)

def fagorGabinete_perfiladoras_fabrica2(request):
    maquina_nome = 'fagorGabinete_perfiladoras_fabrica2'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2/maquinas_perfiladoras_F2/fagorGabinete_perfiladoras_fabrica2.html', context)

def sares2_perfiladoras_fabrica2(request):
    maquina_nome = 'sares2_perfiladoras_fabrica2'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_2/areas_fabrica_2/perfiladoras_fab_2/maquinas_perfiladoras_F2/sares2_perfiladoras_fabrica2.html', context)


def pintura_fabrica2(request):
    return render(request, 'fabrica_2/areas_fabrica_2/pintura_fab_2/pintura_fabrica2.html')

def fabrica3(request):
    return render(request, 'fabrica_3/fabrica3.html')

def prensa_fabrica3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/prensas_F3/prensa_fabrica3.html')

def fagor_prensa_F3(request):
    maquina_nome = 'fagor_prensa_F3'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_3/areas_fabrica_3/prensas_F3/maquinas_prensa_F3/fagor_prensa_F3.html', context)

def Aita_prensa_F3(request):
    maquina_nome = 'Aita_prensa_F3'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_3/areas_fabrica_3/prensas_F3/maquinas_prensa_F3/Aita_prensa_F3.html', context)


def perfiladora_fabrica3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/perfiladoras_F3/perfiladora_fabrica3.html')

def jundiai_perfiladorasF3(request):
    maquina_nome = 'jundiai_perfiladorasF3'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_3/areas_fabrica_3/perfiladoras_F3/maquinas_perfiladoras_F3/jundiai_perfiladorasF3.html', context)

def sares3_perfiladorasF3(request):
    maquina_nome = 'sares3_perfiladorasF3'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_3/areas_fabrica_3/perfiladoras_F3/maquinas_perfiladoras_F3/sares3_perfiladorasF3.html', context)

def sares4_perfiladorasF3(request):
    maquina_nome = 'sares4_perfiladorasF3'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_3/areas_fabrica_3/perfiladoras_F3/maquinas_perfiladoras_F3/sares4_perfiladorasF3.html', context)

def pintura_fabrica3(request):
    return render(request, 'fabrica_3/areas_fabrica_3/pintura_F3/pintura_fabrica3.html')

def pinturaliquidaF3(request):
    maquina_nome = 'pinturaliquidaF3'  
    pecas = Peca.objects.filter(maquina=maquina_nome)

    context = {
        'maquina': maquina_nome,
        'pecas': pecas,
        # outras infos da máquina...
    }
    return render(request, 'fabrica_3/areas_fabrica_3/pintura_F3/maquinas_pintura_F3/pinturaliquidaF3.html', context)








