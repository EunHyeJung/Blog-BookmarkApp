from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark


# ListView
class BookmarkLV(ListView):
    model = Bookmark


# DetailView
class BookmarkDV(DetailView):
    model = Bookmark
