from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from .models import Personagem, Classe, ReferenciasPersonagem
from .forms import PersonagemForm, NovoUsuarioForm

def inicio(request):
    return render(request,'inicio.html', {'nome': 'Nathã Berdeville'})

def entrar(request):
    return render(request, 'entrar.html')

def cadastro_usuario(request):
    formulario = NovoUsuarioForm()
    if request.method == 'POST':
        formulario = NovoUsuarioForm(request.POST)
        if formulario.is_valid():
            if formulario.cleaned_data['password1'] == formulario.cleaned_data['password2']:
                novo_usuario = formulario.save(commit=False)
                novo_usuario.email = formulario.cleaned_data['email']
                novo_usuario.nome = formulario.cleaned_data['nome']
                novo_usuario.sobrenome = formulario.cleaned_data['sobrenome']
                novo_usuario.save()
            return redirect('/login')
        else:
            formulario.add_error('password2', "As senhas não coincidem.")
    return render(request, 'cadastro_usuario.html', {'formulario': formulario})

def login_usuario(request):
    formulario=AuthenticationForm()
    if request.method == 'POST' and request.POST:
        formulario = AuthenticationForm(request, request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            return redirect('/home/')
    return render(request, 'login.html', {'formulario': formulario})

def logout_usuario(request):
 logout(request)
 return redirect('/')

@login_required
def home(request):
    try:
        personagens = Personagem.objects.filter(usuario=request.user).all()
        classes = Classe.objects.all()
        
        for personagem in personagens:
            personagem.description = personagem.descricao.split('\n')
            referencias = personagem.referenciaspersonagem_set.all()
            personagem.referencias = referencias

        for classe in classes:
            classe.description = classe.descricao.split('\n')
            
    except:
        personagens = None
        classes = None

    return render(request, 'home.html', {'usuario':request.user, 'personagens': personagens, 'classes': classes})

@login_required
def detalhes_companion(request,posicao):
    personagens = Personagem.objects.all()
    personagem = personagens.get(pk=posicao)
    personagem.description = personagem.descricao.split('\n')
    referencias = personagem.referenciaspersonagem_set.all()
    personagem.referencias = referencias
    return render(request, 'companion.html', {'personagem': personagem})

def detalhes_classe(request, clase):
    clase_lower = clase.lower()
    classes = Classe.objects.all()
    classe = classes.get(nome__iexact=clase_lower)
    description = classe.descricao.split('\n')
        
    return render(request, 'classe.html', {'classe': classe, 'description':description})

@login_required
def adicionar_dado(request):
    formulario = PersonagemForm()

    if request.method == 'POST' and request.POST:
        formulario = PersonagemForm(request.POST)
        if formulario.is_valid():
            nova_referencia = formulario.save(commit=False)
            nova_referencia.usuario = request.user
            nova_referencia.save()
            return redirect('/home')

    return render(
        request,
        'adicionar_dado.html',
        {'formulario':formulario}
    )

@login_required
def editar_dado(request, id):
    personagens = Personagem.objects.all()
    personagem = get_object_or_404(personagens, id=id,usuario=request.user)
    formulario = PersonagemForm(instance=personagem)
    
    if request.method == 'POST' and request.POST:
        formulario = PersonagemForm(request.POST, instance=personagem)
        if formulario.is_valid():
            formulario.save()
            return redirect('/home')
    
    return render(
        request,
        'editar_dado.html',
        {'formulario': formulario}
    )

@login_required
def remover_dado(request,id):
    personagens = Personagem.objects.all()
    personagem = get_object_or_404(personagens, id=id,usuario=request.user)
    
    
    if request.method == 'POST' and request.POST:
        personagem.delete()
        return redirect('/home')

    return render(
        request,
        'remover_dado.html',
        {'personagem': personagem}
    )