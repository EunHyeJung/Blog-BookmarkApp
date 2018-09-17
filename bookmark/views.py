from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mysite.views import LoginRequiredMixin
# ListView
class BookmarkLV(ListView):
    model = Bookmark


# DetailView
class BookmarkDV(DetailView):
    model = Bookmark


class BookMarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookMarkCreateView, self).form_valid(form)