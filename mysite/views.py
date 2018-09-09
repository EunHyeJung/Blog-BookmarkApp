from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# TmeplateView 제네릭뷰는 필수적으로 template_name 클래스변수를 오버라이딩으로 지정해주어야함.
class HomeView(TemplateView):
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
