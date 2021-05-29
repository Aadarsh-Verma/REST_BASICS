from rest_framework import serializers

from api_basic.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.CharField(required=False)

    class Meta:
        model = Article
        fields = ['id','author','title', 'email']
