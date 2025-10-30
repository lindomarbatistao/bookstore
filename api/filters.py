import django_filters as df
from django.db.models import Q
from .models import Livro, Autor

class LivroFilter(df.FilterSet):
    id = df.NumberFilter(field_name='id', lookup_expr='exact')
    titulo = df.CharFilter(field_name='titulo', lookup_expr='icontains')
    autor = df.CharFilter(method='filter_autor')

    def filter_autor(self, qs, name, value):
        if not value:
            return qs
        return qs.filter(Q(autor__nome__icontains=value) | Q(autor__sobrenome__icontains=value))

    class Meta:
        model = Livro
        fields = '__all__'


class AutorFilter(df.FilterSet):
    nome = df.CharFilter(method='filter_nome')
    nacion = df.CharFilter(field_name='nacion', lookup_expr='iexact')
    
    def filter_nome(self, qs, name, value: str):
        if not value:
            return qs
        return qs.filter(Q(nome__icontains=value) | Q(nacion__icontains=value))

    class Meta:
        model = Autor
        fields = []
