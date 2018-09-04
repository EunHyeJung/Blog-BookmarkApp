from django.views.generic.base import TemplateView

# TmeplateView 제네릭뷰는 필수적으로 template_name 클래스변수를 오버라이딩으로 지정해주어야함.
class HomeView(TemplateView):
    template_name = 'home.html'