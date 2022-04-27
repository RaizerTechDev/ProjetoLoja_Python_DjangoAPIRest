#Relacionamentos Model e Serializers

from rest_framework import serializers

from .models import Categoria, Produto, Avaliacao

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = (
            'id',
            'descricao',
            'criacao',
            'atualizacao',
            'ativo',
        )

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'produto',
            'avaliador',
            'email',
            'comentario',
            'nota',
            'criacao',
            'atualizacao',
            'ativo',
        )

class ProdutoSerializer(serializers.ModelSerializer):

  # Nested Relationship - many  --> muitas avaliaçoes
  # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

  # HyperLinked Related Field
  avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

  # Primary Key Relate Field
  # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
     model = Produto
     fields = [
         'id',
         'nome',
         'preco',
         'categoria',
         'criacao',
         'atualizacao',
         'ativo',
         'avaliacoes',
     ]







