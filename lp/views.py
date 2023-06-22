from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Leads, Perfil, Tagmeta, TagGoogle, LandingPage, Carousel, ItemEmprrendimento
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, time
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect


# Create your views here.


def index(request):
    if request.method == 'POST':
        nome_leads = request.POST.get('nome')
        email_leads = request.POST.get('email')
        whatsapp_leads = request.POST.get('whatsapp')
        status_aberto = 'fa-envelope'
        status_leads = 'NEUTRO'
        data_recebimento = datetime.now()
        Leads.objects.create(nome_leads=nome_leads,
                             email=email_leads,
                             whatsapp=whatsapp_leads,
                             status_aberto=status_aberto,
                             status_leads=status_leads,
                             data_recebimento=data_recebimento)
        leads = Leads.objects.last()

        return render(request, 'site/vale-dos-campos-.html')
    else:
        tag_meta = Tagmeta.objects.all()

        return render(request, 'site/vale-dos-campos-.html', {'tag_meta': tag_meta})


def abrirleads(request, pk):
    status_aberto = 'fa-envelope-open'
    Leads.objects.filter(pk=pk).update(status_aberto=status_aberto)


@login_required
def dashboard(request):
    leads = Leads.objects.all().order_by('-data_recebimento')
    return render(request, 'site/dashboard-v3.html', {'leads': leads})


def qualificar_leads(request, pk):
    if request.method == 'POST':
        status_leads = request.POST.get('opcionais-leads')
        print(status_leads)
        Leads.objects.filter(pk=pk).update(status_leads=status_leads)
        return redirect('atendimento', pk=pk)


def excluir_leads(request, pk):
    if request.method == 'POST':
        leads_excluir = Leads.objects.filter(pk=pk)
        leads_excluir.delete()
        return redirect('dashboard')
    else:
        return redirect('index')


@login_required
def configuracao(request, user):
    meta_tag = Tagmeta.objects.all()
    tag_google = TagGoogle.objects.all()
    logado = request.user.username
    if user == logado:
        perfil = Perfil.objects.filter(user_vinculado=user)
        print(perfil)
        return render(request, 'site/configuracao.html', {'perfil': perfil,
                                                          'user': user,
                                                          'meta_tag': meta_tag,
                                                          'tag_google': tag_google})
    else:
        return redirect(reverse('configuracao', args=[request.user]))


def add_img_perfil(request):
    if request.method == 'POST':
        img_perfil = request.FILES.get('img_perfil_add')
        user_vinculado = request.POST.get('user_vinculado')
        Perfil.objects.create(img_perfil=img_perfil,
                              user_vinculado=user_vinculado)
        return redirect(reverse('configuracao', args=[request.user]))


def editar_img_perfil(request):
    if request.method == 'POST':
        img_perfil = request.FILES.get('img_perfil_editar')
        user_vinculado = request.POST.get('user_vinculado_editar')
        Perfil.objects.get(user_vinculado=user_vinculado).delete()
        Perfil.objects.create(img_perfil=img_perfil,
                              user_vinculado=user_vinculado)
        return redirect(reverse('configuracao', args=[request.user]))


def landingpage(request, slug):
    empreendimento = get_object_or_404(LandingPage, slug=slug)
    nome_relacionado = empreendimento.nome_empreendimento
    # print(nome_relacionado)
    carroussel_vinculado = Carousel.objects.filter(empreendimento_relacionado=nome_relacionado)
    itens_vinculado = ItemEmprrendimento.objects.filter(empreendimento_relacinado=nome_relacionado)
    print(itens_vinculado)
    # print(carroussel_vinculado)
    return render(request, 'site/landing-page.html', {'empreendimento': empreendimento,
                                                      'carroussel_vinculado': carroussel_vinculado,
                                                      'itens_vinculado': itens_vinculado})


@login_required
def dashboard_lp(request):
    if request.method == 'POST':
        nome_empreendimento = request.POST.get('nome_empreendimento')
        localizacao_empreendimento = request.POST.get('localizacao_empreendimento')
        data_atual = datetime.now()
        user_logado = request.user.username
        itens = request.POST.getlist('item_adicionado')
        for i in itens:
            ItemEmprrendimento.objects.create(empreendimento_relacinado=nome_empreendimento,
                                              item_empreendimento=i
                                              )
        LandingPage.objects.create(nome_empreendimento=nome_empreendimento,
                                   localizacao=localizacao_empreendimento,
                                   data_cadastramento=data_atual,
                                   user_cadastramento=user_logado
                                   )
        lp = LandingPage.objects.last()
        return render(request, 'site/upload-img.html', {'lp': lp})
    else:
        lista_lp = LandingPage.objects.all()
        busca = request.GET.get('barra-pesquisa')
        if busca:
            lista_lp = LandingPage.objects.filter(Q(nome_empreendimento__icontains=busca))

        return render(request, 'site/dashboard-lp.html', {'lista_lp': lista_lp, 'busca': busca})


@login_required
def cadastro_lp(request, slug):
    nome_empreendimento = get_object_or_404(LandingPage, slug=slug)
    return render(request, 'site/cadastro-lp.html', {'nome_empreendimento': nome_empreendimento.nome_empreendimento})


def cadastrar_lp(request):
    if request.method == 'POST':
        nome_empreendimento = request.POST.get('nome_empreendimento')
        localizacao_empreendimento = request.POST.get('localizacao_empreendimento')

        LandingPage.objects.create(nome_empreendimento=nome_empreendimento, localizacao=localizacao_empreendimento)
        lp = LandingPage.objects.last()
        print(lp)

        return redirect(reverse('upload_img', args=[lp.nome_empreendimento]))
    else:

        return render(request, 'site/dashboard-lp.html')


def upload_img(request):
    if request.method == 'POST':
        empreendimento_vinculado = request.POST.get('empreendimento_vinculado')
        print(empreendimento_vinculado)
        imagem = request.FILES.get('file')
        print(imagem)
        Carousel.objects.create(empreendimento_relacionado=empreendimento_vinculado, imagens=imagem)
        return redirect('add-itens-destaque', args=[empreendimento_vinculado])
    else:
        return render(request, 'site/upload-img.html')


def add_itens_destaque(request, slug):
    return render(request, 'site/add-itens-empreendimento.html')
