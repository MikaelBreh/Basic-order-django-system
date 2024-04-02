from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Clientes


# Create your views here.
def home(request):
    return render(request, 'cadastros/listas.html')


class ClientesList(ListView):
    model = Clientes
    template_name = 'cadastros/listas.html'




class ClienteCreate(CreateView):
    model = Clientes
    fields = ['nome_fantasia', 'razao_social', 'cnpj', 'inscricao_estadual', 'cep', 'endereco', 'cidade']
    template_name = 'cadastros/cadastro.html'
    success_url = '/cadastro/'
