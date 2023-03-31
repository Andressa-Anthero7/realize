from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/login/dashboard/',views.dashboard,name='dashboard'),
    path('atendimento/<int:pk>/', views.atendimento, name='atendimento'),
    path('criar_agendamento/', views.criar_agendamento, name='criar_agendamento'),
    path('criar_atendimento/', views.criar_atendimento, name='criar_atendimento'),
    path('abrirleads/<int:pk>/', views.abrirleads, name='abrirleads'),
    path('cadastrar_clientes/', views.cadastrar_clientes, name='cadastrar_clientes'),
    path('cadastro_cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('qualificar_leads/<int:pk>/', views.qualificar_leads, name='qualificar_leads'),
    path('leads_excluir/<int:pk>/', views.excluir_leads, name='excluir_leads'),
    path('editar_agendamento/<int:pk>/', views.editar_agendamento, name='editar_agendamento'),
    path('configuracao/<str:user>/', views.configuracao, name='configuracao'),
    path('add_img_perfil/', views.add_img_perfil, name='add_img_perfil'),
    path('editar_img_perfil/', views.editar_img_perfil, name='editar_img_perfil'),
    path('add_meta_tag/', views.add_meta_tag, name='add_meta_tag'),

]
