from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro  # Certifique-se de que o nome do modelo está correto
from .forms import LivroForm
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages



# Função para listar livros
def listar_livros(request):
    livros = Livro.objects.all()  # Corrigido de 'livros' para 'Livros'
    return render(request, 'livros/listar_livros.html', {'livros': livros})

# Função para criar livros
def criar_livros(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
       
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro criado com sucesso!')
            return redirect('listar_livros')
        else:
            print(form.errors)
    else:
        form = LivroForm()  # Inicializa o formulário no caso de requisição GET
    
    return render(request, 'livros/criar_livros.html', {'form': form})


# Função para atualizar livros
def atualizar_livros(request, id):
    livros = get_object_or_404(Livro, id=id)  # Carrega o livro pela ID
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livros)  # Instância é importante para edição
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livros)  # Preenche o formulário com os dados existentes do livro
    return render(request, 'livros/atualizar_livros.html', {'form': form})

# Função para deletar livros
def deletar_livros(request, id):
    livros = get_object_or_404(Livro, id=id)  # Corrige a referência para o modelo Livros
    if request.method == "POST":
        livros.delete()
        return redirect('listar_livros')
    return render(request, 'livros/deletar_livros.html', {'livros': livros})

# Função para exportar livros em PDF
def exportar_livros_pdf(request):
    livros = Livro.objects.all()  # Corrige a referência para o modelo Livros

    html_string = render_to_string('livros/livros_pdf.html', {'livros': livros})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="livros.pdf"'

    HTML(string=html_string).write_pdf(response)

    return response
