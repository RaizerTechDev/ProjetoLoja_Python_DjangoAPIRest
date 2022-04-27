"""
API V1
"""
from rest_framework import generics
from rest_framework.generics import get_object_or_404



from rest_framework import views

from .models import Categoria, Produto, Avaliacao
from .serializers import ProdutoSerializer, CategoriaSerializer, AvaliacaoSerializer

class ProdutosAPIView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        if self.kwargs.get('categoria_pk'):
            return self.queryset.filter(categoria_id=self.kwargs.get('categoria_pk'))
        return self.queryset.all()


class ProdutoAPIView(generics.RetrieveUpdateDestroyAPIView):
      queryset = Produto.objects.all()
      serializer_class = ProdutoSerializer

      def get_object(self):
          if self.kwargs.get('categoria_pk'):
              return get_object_or_404(self.get_queryset(),
                                        categoria_id=self.kwargs.get('categoria_pk'),
                                        pk=self.kwargs.get('produto_pk'))
          return get_object_or_404(self.get_queryset(),
                                    pk=self.kwargs.get('produto_pk'))



class CategoriasAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all ()
    serializer_class = CategoriaSerializer

class AvaliacoesAPIViews(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('produto_pk'):
            return self.queryset.filter(produto_id=self.kwargs.get('produto_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('produto_pk'):
            return get_object_or_404 (self.get_queryset(),
                                      produto_id=self.kwargs.get('produto_pk'),
                                      pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(),
                                  pk=self.kwargs.get('avaliacao_pk'))




















