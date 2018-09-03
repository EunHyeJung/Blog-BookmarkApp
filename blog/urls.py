from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # Example : /
    path('', PostLV.as_view(), name='index'),
    # Example : /post/
    path('post/', PostLV.as_view(), name='post_list'),
    # Example : /post/slug/
    path('post/<slug:slug>/', PostDV.as_view(), name='post_detail'),
    # Example : /archive/
    path('archive/', PostAV.as_view(), name='post_archive'),

    # Example : /2018/
    path('<int:year>/', PostYAV.as_view(), name='post_year_archive'),
    # Example : /2018/sep/
    path('<int:year>/<int:month>/', PostMAV.as_view, name='post_month_archive'),
    # Example : /2018/sep/10
    path('<int:year>/<int:month>/<int:day>/', PostDAV.as_view, name='post_day_archive'),

    # Example : /today/
    path('today/', PostTAV.as_view, name = 'post_today_archive')
]
