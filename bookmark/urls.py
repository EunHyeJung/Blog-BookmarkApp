from django.urls import path, include
from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    path('bookmark/', BookmarkLV.as_view(), name = 'index'),
    path('bookmark/<int:pk>', BookmarkDV.as_view(), name = 'detail'),
]
