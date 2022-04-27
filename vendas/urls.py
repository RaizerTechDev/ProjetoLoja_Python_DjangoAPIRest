from django.urls import path
from .views_antigo import CategoriasAPIView, ProdutosAPIView, AvaliacoesAPIView
from .views import CategoriaAPIView, ProdutoAPIView, AvaliacaoAPIView

# Versão 2
from .viewsAPIV2 import ProdutoViewSet, AvaliacaoViewSet, CategoriaViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('produtos', ProdutoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)
router.register('categorias', CategoriaViewSet)

urlpatterns = [
    path('categorias/', CategoriasAPIView.as_view(), name='categorias'),
    path('categorias/<int:pk>/', CategoriaAPIView.as_view(), name='categoria'),

    path('produtos/', ProdutosAPIView.as_view(), name='produtos'),
    path('produtos/<int:produto_pk>/', ProdutoAPIView.as_view(), name='produto'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
 ################################
    path('produtos/<int:produto_pk>/avaliacoes/',
          AvaliacoesAPIView.as_view(),
          name='produto_avaliacoes'),

    path('produtos/<int:produto_pk>/avaliacoes/<int:avaliacao_pk>/',
          AvaliacaoAPIView.as_view(), name='produto_avaliacao'),

    path('avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view (), name='avaliacao'),

    path('categorias/<int:categoria_pk>/produtos/',
          ProdutosAPIView.as_view(),
          name='categoria_produto'),

    path ('categorias/<int:categoria_pk>/produtos/<int:produto_pk>/',
          ProdutoAPIView.as_view(),
          name='categoria_produto'),

]

