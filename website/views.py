from django.shortcuts import render, redirect
from website.models import Pessoa, Ideia

# Create your views here.

def index(request):
    #essa página vai cadastrar uma pessoa
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        contexto = {'msg': 'Parabéns, agora só colocar seu e-mail'}
        return render(request, 'login.html', contexto)

    return render(request, 'index.html', contexto)


def sobre(request):
    #essa página vai listar as ideias e seus criadores
    ideias = Ideia.objects.all()
    contexto = {
        'ideias':ideias
    }
    return render(request, 'sobre.html', contexto)

def login(request):
    # Essa página irá conferir se existe um usuário
    # cadastrado, se sim retonará para página sobre
    # se não, retornará para página de cadastro com
    # uma mensagem "Cadastre-se para criar uma ideia"
    if request.method == 'POST':
        email_form = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_form).first()

        print('Iae meu bom amigo ', pessoa)

        if pessoa is None:
            #mandar para página de cadastro
            contexto = {'msg': 'Cadastre-se para criar uma ideia'}
            return render(request, 'index.html', contexto)
        else:
            #mandar para página de ideias
            contexto = {'pessoa': pessoa}
            return render(request, 'ideias.html', contexto)

    return render(request, 'login.html', {})

def cadastrar_ideia(request):
    if request.method == 'POST':
        email_pessoa = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_pessoa).first()
        if pessoa is not None:
            ideia = Ideia()
            ideia.pessoa = pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categoria = request.POST.get('categoria')
            ideia.categoria_outros = request.POST.get('categoria_outros')
            ideia.save()
            print('uhuuu')

            return redirect('/sobre') 

    return render(request, 'ideias.html', {}) 