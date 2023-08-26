from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/login/dashboard/', views.dashboard, name='dashboard'),
    path('abrirleads/<int:pk>/', views.abrirleads, name='abrirleads'),
    path('leads_excluir/<int:pk>/', views.excluir_leads, name='excluir_leads'),
    path('configuracao/<str:user>/', views.configuracao, name='configuracao'),
    path('add_img_perfil/', views.add_img_perfil, name='add_img_perfil'),
    path('editar_img_perfil/', views.editar_img_perfil, name='editar_img_perfil'),
    path('<int:pk>/<slug:slug>/', views.landingpage, name='landingpage'),
    path('accounts/login/adicionar-veiculo/', views.dashboard_lp, name='adicionar-veiculo'),
    path('accounts/login/cadastro-lp/<slug:slug>/', views.cadastro_lp, name='cadastro-lp'),
    path('accounts/login/cadastrar-lp/upload-img/', views.upload_img, name='upload-img'),
    path('accounts/login/estoque-veiculos/', views.estoque_veiculos, name='estoque-veiculos'),
    path('deletar_lp/<int:pk>/', views.deletar_lp, name='deletar-lp'),


]
