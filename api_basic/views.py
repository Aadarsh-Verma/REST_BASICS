from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import generics
from api_basic.models import Article
from api_basic.serializers import ArticleSerializer


@api_view(['GET', ])
def ArticleListAPI(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ArticleViewAPI(request, pk):
    print(request.user)
    articles = Article.objects.get(pk=pk)
    print(articles.author)
    if request.method == 'GET':
        serializers = ArticleSerializer(articles)
        if str(request.user) == str(articles.author):
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            context = {'Permission Denied': 'You are not the author'}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def ArticleCreateAPI(request):
    if request.method == 'POST':
        print(request.data)
        serializer = ArticleSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            author = serializer.validated_data['author']
            author = User.objects.get(username=author)
            serializer.save(author=author)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListArticlesAPI(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        items = Article.objects.all()
        return items

    def perform_create(self, serializer):
        author = self.request.user
        user = User.objects.get(username=author)
        serializer.save(author=user)


class DeleteArticlesAPI(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def delete(self, request, pk, *args, **kwargs):
        temp = Article.objects.get(pk=pk)
        temp.delete()
        return Response({'data': 'The given value is deleted'},
                        status=status.HTTP_200_OK)
