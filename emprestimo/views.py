# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Alocacao
from gerencialivro.models import Livro
from django.utils import timezone
from django.contrib import messages

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

def nova_alocacao(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    print(f"Livro encontrado: {livro.titulo}")  # Verifique se isso é impresso no console
    return render(request, 'emprestimo/nova_alocacao.html', {'livro': livro})

    

from django.shortcuts import render
from .models import Livro, Alocacao

def lista_alocacoes(request):
    livros = Livro.objects.all()  # Carrega todos os livros para exibir no template
    alocacoes = Alocacao.objects.filter(ativo=True)  # Filtra as alocações ativas
    return render(request, 'emprestimo/lista_alocacoes.html', {
        'livros': livros,
        'alocacoes': alocacoes,
    })


def finalizar_alocacao(request, alocacao_id):
    alocacao = get_object_or_404(Alocacao, id=alocacao_id)
    alocacao.finalizar_alocacao()
    messages.success(request, f"O livro '{alocacao.livro.titulo}' foi devolvido com sucesso.")
    return redirect('lista_alocacoes')

def exportar_alocacoes_pdf(request):
    # Recuperar todas as alocações ativas
    alocacoes = Alocacao.objects.filter(ativo=True)

    # Renderizar o template de alocação para o PDF
    html_string = render_to_string('emprestimo/alocacoes_pdf.html', {'alocacoes': alocacoes})

    # Gerar o PDF
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    # Retornar o PDF como resposta HTTP
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="alocacoes_ativas.pdf"'
    return response