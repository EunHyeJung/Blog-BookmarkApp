from django.urls import path, include
from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
