from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from .models import Usuario
from django.contrib import messages
from weasyprint import HTML
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


Usuario = get_user_model()

@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()  # Supondo que você tenha um modelo Usuario
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})
    

 # Certifique-se de que você tem o modelo correto
@login_required
def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario =  form.save()  # Salva o usuário se o formulário for válido
            print(usuario)
            return redirect('listar_usuarios')  # Redireciona após salvar
        else:
            # Exibe os erros de validação no template
            print(form.errors)
            return render(request, 'usuarios/registrar_usuario.html', {'form': form})  # Renderiza com erros
    else:
        form = UsuarioForm()

    # Renderiza o formulário vazio caso seja um GET
    return render(request, 'usuarios/registrar_usuario.html', {'form': form})
    
@login_required
def usuario_pdf(request):
    usuario = Usuario.objects.all()

    html_string = render_to_string('usuarios/usuario_pdf.html', {'usuario': usuario})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="usuario.pdf"'

    HTML(string=html_string).write_pdf(response)

    return response

@login_required
def atualizar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')  # Redireciona após atualizar
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/atualizar_usuario.html', {'form': form})

@login_required
def deletar_usuarios(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)  # Obtém o usuário com base no ID
    if request.method == 'POST':
        usuario.delete()  # Deleta o usuário
        messages.success(request, 'Usuário deletado com sucesso!')
        return redirect('listar_usuarios')  # Redireciona após a exclusão
    return render(request, 'usuarios/deletar_usuario.html', {'usuario': usuario})  # Corrigido para o nome correto do template
