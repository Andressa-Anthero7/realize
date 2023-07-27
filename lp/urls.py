from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/login/dashboard/', views.dashboard, name='dashboard'),
    path('abrirleads/<int:pk>/', views.abrirleads, name='abrirleads'),
    path('qualificar_leads/<int:pk>/', views.qualificar_leads, name='qualificar_leads'),
    path('leads_excluir/<int:pk>/', views.excluir_leads, name='excluir_leads'),
    path('configuracao/<str:user>/', views.configuracao, name='configuracao'),
    path('add_img_perfil/', views.add_img_perfil, name='add_img_perfil'),
    path('editar_img_perfil/', views.editar_img_perfil, name='editar_img_perfil'),
    path('<slug:slug>/', views.landingpage, name='landingpage'),
    path('accounts/login/gerenciador-lp/', views.dashboard_lp, name='dashboard-lp'),
    path('accounts/login/cadastro-lp/<slug:slug>/', views.cadastro_lp, name='cadastro-lp'),
    path('accounts/login/gerenciador-lp/upload-img/', views.upload_img, name='upload-img'),

]
