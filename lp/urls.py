from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('atendimento/', views.atendimento, name='atendimento'),
    path('criar_agendamento/', views.criar_agendamento, name='criar_agendamento'),

]