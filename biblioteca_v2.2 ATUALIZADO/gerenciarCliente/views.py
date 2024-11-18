from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
#from django.contrib.auth.decorators import login_required

from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import render_to_string


def lista_clientes(request):  
    clientes = Cliente.objects.all()
    print(clientes)  # Adicione isso para verificar a saída no console
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def criar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/criar_clientes.html', {'form': form})

def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/atualizar_cliente.html', {'form': form})

def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/deletar_cliente.html', {'cliente': cliente})

#@login_required
def exportar_cliente_pdf(request):
    # Buscando todos os usuários
    clientes = Cliente.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('clientes/cliente_pdf.html', {'clientes': clientes})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="cliente.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response

