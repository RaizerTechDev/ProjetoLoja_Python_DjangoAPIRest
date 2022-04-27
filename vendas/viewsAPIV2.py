"""
API V2
"""
from rest_framework import generics, mixins

from rest_framework import viewsets

from .models import Categoria, Produto, Avaliacao

from .serializers import ProdutoSerializer, CategoriaSerializer, AvaliacaoSerializer

from rest_framework.decorators import action

from rest_framework.response import Response

from rest_framework import permissions

from .permissions import VerSuperUsuario


class ProdutoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        VerSuperUsuario,
        permissions.DjangoModelPermissions,)
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(produto_id=pk)
        page = self.paginate_queryset(avaliacoes)
        if page:
         serializer = AvaliacaoSerializer(page, many=True)
         return self.get_paginated_response(serializer.data)
         serializer = AvaliacaoSerializer(avaliacoes, many=True)
         return Response(serializer.data)

class AvaliacaoViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


