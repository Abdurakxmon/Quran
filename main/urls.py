from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('<str:surai_slug>', views.SuraiViewDetail.as_view(), name='surai_detail'),
    path('result',views.search, name='search')
]