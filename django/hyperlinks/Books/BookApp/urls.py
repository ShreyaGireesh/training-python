from django.urls import path
from . import views

urlpatterns = [
    # Non-hyperlinked API
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # Hyperlinked API
    path('authors-hyperlinked/', views.AuthorHyperlinkedListView.as_view(), name='author-hyperlinked-list'),
    path('authors-hyperlinked/<int:pk>/', views.AuthorHyperlinkedDetailView.as_view(), name='author-hyperlinked-detail'),
    path('books-hyperlinked/', views.BookHyperlinkedListView.as_view(), name='book-hyperlinked-list'),
    path('books-hyperlinked/<int:pk>/', views.BookHyperlinkedDetailView.as_view(), name='book-hyperlinked-detail'),
]
