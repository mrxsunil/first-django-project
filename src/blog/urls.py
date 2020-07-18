from django.urls import path 
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = 'article'
urlpatterns = [
    path('',ArticleListView.as_view(),name='article-list'),
    path('<int:pk>',ArticleDetailView.as_view(),name='article-details'),
    path('<int:pk>/update/',ArticleUpdateView.as_view(),name='article-update'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='article-delete'),
    path('create/',ArticleCreateView.as_view(),name='article-create')
]
