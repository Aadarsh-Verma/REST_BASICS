from django.urls import path

from api_basic.views import ArticleCreateAPI, ArticleListAPI, ArticleViewAPI, ListArticlesAPI, DeleteArticlesAPI

urlpatterns = [
    path('create/', ArticleCreateAPI, name='create_api'),
    path('list/', ArticleListAPI, name='list_api'),
    path('view/<pk>/', ArticleViewAPI, name='view_api'),
    path('genericlist/', ListArticlesAPI.as_view(), name='list_generic'),
    path('delete/<pk>/', DeleteArticlesAPI.as_view(), name='delete'),
]
