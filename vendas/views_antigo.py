from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Categoria, Produto, Avaliacao
from .serializers import CategoriaSerializer, ProdutoSerializer, AvaliacaoSerializer

class CategoriasAPIView(APIView):
     """
      API para categorias do produto
     """
     def get(self, request):
         categorias = Categoria.objects.all()
         serializer = CategoriaSerializer(categorias, many=True)
         return Response(serializer.data)

     def post(self, request):
         serializer = CategoriaSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response ({"id": serializer.data['id'], "descricao":serializer.data['descricao']}, status=status.HTTP_201_CREATED)

class ProdutosAPIView(APIView):
       """
         API para produtos
       """
       def get(self, request):
          produtos = Produto.objects.all()
          serializer = ProdutoSerializer(produtos, many=True)
          return Response(serializer.data)

       def post(self, request):
           serializer = ProdutoSerializer(data=request.data)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response ({"mensagem": "cadastrado com sucesso!!!"}, status=status.HTTP_201_CREATED)


class AvaliacoesAPIView (APIView):
    """
      API para avaliacoes do produto
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response (serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response ({"mensagem": "cadastrado com sucesso!!!"}, status=status.HTTP_201_CREATED)


