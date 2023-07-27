from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Leads, Perfil, Tagmeta, TagGoogle, LandingPage, Carousel, ItensDestaque
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import spacy
import requests

# Create your views here.

# Substitua "SUA_CHAVE_DE_API" pela sua chave de API do Google Maps
chave = "AIzaSyA6EVGvxZFbZ1wg_5pP9onIn9FQeh1VBFY"


def juntar_palavras_compostas(palavras):
    # Defina aqui os termos compostos e suas respectivas junções.
    termos_compostos = {
        "1": "1 quarto",
        "2": "2 quartos",
        "Sacada": "Sacada",
        "Sacada Gourmet": "Sacada Gourmet",
        "2 vagas": "2 vagas na garagem",
        "vagas": "2 vagas na garagem",
        "Casa": "Casa",
        "Casas": "Casa",  # Inclusão de "Casas" como sinônimo de "Casa"
        "Alto Padrao": "Alto Padrão",
        "Apartamentos": "Apartamento",  # Inclusão de "Apartamentos" como sinônimo de "Apartamento"
        # Adicione mais termos compostos e suas respectivas junções, se necessário.
    }

    # Verifica se as palavras estão presentes no dicionário de termos compostos.
    termo_composto = " ".join(palavras)
    if termo_composto in termos_compostos:
        return termos_compostos[termo_composto]

    # Se as palavras não formam um termo composto, simplesmente retorna as palavras individuais concatenadas.
    return


def index(request):
    pesquisa = request.GET.get('barra-pesquisa')

    # se é pesquisa
    if pesquisa:
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {"address": pesquisa, "key": chave}

        response = requests.get(base_url, params=params)
        data = response.json()

        if data["status"] == "OK" and pesquisa not in 'alto':
            # Obter as coordenadas geográficas
            location = data["results"][0]["geometry"]["location"]
            lat = location["lat"]
            long = location["lng"]
            coordenadas = lat, long
            print('coordenadas são', coordenadas)
            listagem = LandingPage.objects.all()
            # Calcular a distância entre a geolocalização e Araraquara
            araraquara_coords = (-21.7845, -48.1783)  # Coordenadas de Araraquara
            distance_to_araraquara = geodesic(coordenadas, araraquara_coords).kilometers
            # Se a distância da pesquisa  for maior que 25 km, não fazer a pesquisa
            print('distancia araraquara', distance_to_araraquara)
            distancia_araraquara = int(distance_to_araraquara)
            landing_page_proxima = []
            print(distancia_araraquara)
            print(type(distancia_araraquara))
            raio = int(25)
            print(type(raio))
            # se distancia de araraquara maiaor que 25
            if distancia_araraquara < raio:
                print('pesquisa esta no raio de 25 km Araraquara')
                # para cada landing page na lista eu vou fazer a consulta do ponto de pesquisa ate a mesma
                for landing_page in listagem:
                    distancia_ponto_pesquisa = geodesic((landing_page.latitude, landing_page.longitude),
                                                        coordenadas).kilometers
                    distancia_ponto_pesquisa = int(distancia_ponto_pesquisa)
                    if distancia_ponto_pesquisa < 3:
                        landing_page_proxima.append(landing_page)

                    print('distancia ponto de pesquisa', distancia_ponto_pesquisa)
                print('pesquisa por proximdade geografica')
                return render(request, 'site/index.html', {'listagem': landing_page_proxima})
            else:
                lista_split = ['com', 'que tenha', 'que tem', 'c/', 'perto', 'da', 'de', 'di', 'do', 'du', 'proximo',
                               'próximo', 'na', 'no', 'em', 'e', 'ou', 'que', 'tem', 'area']

                palavras_chaves = []

                pesquisa = pesquisa.split()

                for palavra in pesquisa:
                    if palavra not in lista_split:
                        palavras_chaves.append(palavra)
                    if palavra == 'casas':
                        palavra = 'casa'
                        palavras_chaves.append(palavra)
                    if palavra == 'apartamentos':
                        palavra = 'apartamento'
                        palavras_chaves.append(palavra)
                print('as palavras chaves processada:', palavras_chaves)

                conditions = Q()
                for keyword in palavras_chaves:
                    keywords_compostas = juntar_palavras_compostas(keyword)
                    # se for palavra composta
                    if keywords_compostas is not None:
                        print('keywords composta', keywords_compostas)
                        conditions |= Q(tipo_imovel__iexact=keywords_compostas)
                        conditions |= Q(status_imovel__iexact=keywords_compostas)
                        conditions |= Q(padrao_imovel__iexact=keywords_compostas)
                        conditions |= Q(nome_empreendimento__iexact=keywords_compostas)
                        conditions |= Q(localizacao__iexact=keywords_compostas)
                        conditions |= Q(item_1__iexact=keywords_compostas)
                        conditions |= Q(item_2__iexact=keywords_compostas)
                        conditions |= Q(item_3__iexact=keywords_compostas)
                        conditions |= Q(item_4__iexact=keywords_compostas)
                        conditions |= Q(item_5__iexact=keywords_compostas)
                        conditions |= Q(item_6__iexact=keywords_compostas)
                        conditions |= Q(item_7__iexact=keywords_compostas)
                        listagem = LandingPage.objects.filter(conditions)
                        print('Pesquisa por palavra-chave composta', listagem)
                        return render(request, 'site/index.html', {'listagem': listagem})
                    # se NAO FOR palavra simples
                    if keywords_compostas is None:
                        keyword_separada = keyword
                        print('key word não composta', keyword_separada)
                        conditions |= Q(tipo_imovel__iexact=keyword_separada)
                        conditions |= Q(status_imovel__iexact=keyword_separada)
                        conditions |= Q(padrao_imovel__iexact=keyword_separada)
                        conditions |= Q(nome_empreendimento__iexact=keyword_separada)
                        conditions |= Q(localizacao__iexact=keyword_separada)
                        conditions |= Q(item_1__iexact=keyword_separada)
                        conditions |= Q(item_2__iexact=keyword_separada)
                        conditions |= Q(item_3__iexact=keyword_separada)
                        conditions |= Q(item_4__iexact=keyword_separada)
                        conditions |= Q(item_5__iexact=keyword_separada)
                        conditions |= Q(item_6__iexact=keyword_separada)
                        conditions |= Q(item_7__iexact=keyword_separada)
                        listagem = LandingPage.objects.filter(conditions)
                        print('Pesquisa por palavra-chave simples', listagem)
                        if listagem:
                            print('é listagem por palavra chave simples cheia')
                            return render(request, 'site/index.html', {'listagem': listagem})
                        else:
                            conditions |= Q(tipo_imovel__icontains=keyword_separada)
                            conditions |= Q(status_imovel__icontains=keyword_separada)
                            conditions |= Q(padrao_imovel__icontains=keyword_separada)
                            conditions |= Q(nome_empreendimento__icontains=keyword_separada)
                            conditions |= Q(localizacao__icontains=keyword_separada)
                            conditions |= Q(item_1__icontains=keyword_separada)
                            conditions |= Q(item_2__icontains=keyword_separada)
                            conditions |= Q(item_3__icontains=keyword_separada)
                            conditions |= Q(item_4__icontains=keyword_separada)
                            conditions |= Q(item_5__icontains=keyword_separada)
                            conditions |= Q(item_6__icontains=keyword_separada)
                            conditions |= Q(item_7__icontains=keyword_separada)
                            listagem = LandingPage.objects.filter(conditions)
                            print('é listagem vazia  por palavra chave simples passando', keyword_separada)
                            return render(request, 'site/index.html', {'listagem': listagem})
        else:
            lista_split = ['com', 'que tenha', 'que tem', 'c/', 'perto', 'da', 'de', 'di', 'do', 'du', 'proximo',
                           'próximo', 'na', 'no', 'em', 'e', 'ou', 'que', 'tem', 'area']

            palavras_chaves = []

            pesquisa = pesquisa.split()

            for palavra in pesquisa:
                if palavra not in lista_split:
                    palavras_chaves.append(palavra)
                if palavra == 'casas':
                    singular = 'casa'
                    palavras_chaves.append(singular)
                if palavra == 'apartamentos':
                    singular = 'apartamento'
                    palavras_chaves.append(singular)
            print('as palavras chaves processada:3', palavras_chaves)

            conditions = Q()
            for keyword in palavras_chaves:
                keywords_compostas = juntar_palavras_compostas(keyword)
                # se for palavra composta
                if keywords_compostas is not None:
                    print('keywords composta', keywords_compostas)
                    conditions |= Q(tipo_imovel__iexact=keywords_compostas)
                    conditions |= Q(status_imovel__iexact=keywords_compostas)
                    conditions |= Q(padrao_imovel__iexact=keywords_compostas)
                    conditions |= Q(nome_empreendimento__iexact=keywords_compostas)
                    conditions |= Q(localizacao__iexact=keywords_compostas)
                    conditions |= Q(item_1__iexact=keywords_compostas)
                    conditions |= Q(item_2__iexact=keywords_compostas)
                    conditions |= Q(item_3__iexact=keywords_compostas)
                    conditions |= Q(item_4__iexact=keywords_compostas)
                    conditions |= Q(item_5__iexact=keywords_compostas)
                    conditions |= Q(item_6__iexact=keywords_compostas)
                    conditions |= Q(item_7__iexact=keywords_compostas)
                    listagem = LandingPage.objects.filter(conditions)
                    print('Pesquisa por palavra-chave composta', listagem)
                    return render(request, 'site/index.html', {'listagem': listagem})
                # se NAO FOR palavra simples
                if keywords_compostas is None:
                    keyword_separada = keyword
                    if keyword_separada == 'casas':
                        singular = 'casa'
                        keyword_separada = singular
                    if keyword_separada == 'apartamentos':
                        singular = 'apartamento'
                        keyword_separada = singular
                    print('key word não composta', keyword_separada)
                    conditions |= Q(tipo_imovel__iexact=keyword_separada)
                    conditions |= Q(status_imovel__iexact=keyword_separada)
                    conditions |= Q(padrao_imovel__iexact=keyword_separada)
                    conditions |= Q(nome_empreendimento__iexact=keyword_separada)
                    conditions |= Q(localizacao__iexact=keyword_separada)
                    conditions |= Q(item_1__iexact=keyword_separada)
                    conditions |= Q(item_2__iexact=keyword_separada)
                    conditions |= Q(item_3__iexact=keyword_separada)
                    conditions |= Q(item_4__iexact=keyword_separada)
                    conditions |= Q(item_5__iexact=keyword_separada)
                    conditions |= Q(item_6__iexact=keyword_separada)
                    conditions |= Q(item_7__iexact=keyword_separada)
                    listagem = LandingPage.objects.filter(conditions)
                    print('Pesquisa por palavra-chave simples', listagem)
                    if listagem:
                        print('é listagem por palavra chave simples cheia')
                        return render(request, 'site/index.html', {'listagem': listagem})
                    else:
                        conditions |= Q(tipo_imovel__icontains=keyword_separada)
                        conditions |= Q(status_imovel__icontains=keyword_separada)
                        conditions |= Q(padrao_imovel__icontains=keyword_separada)
                        conditions |= Q(nome_empreendimento__icontains=keyword_separada)
                        conditions |= Q(localizacao__icontains=keyword_separada)
                        conditions |= Q(item_1__icontains=keyword_separada)
                        conditions |= Q(item_2__icontains=keyword_separada)
                        conditions |= Q(item_3__icontains=keyword_separada)
                        conditions |= Q(item_4__icontains=keyword_separada)
                        conditions |= Q(item_5__icontains=keyword_separada)
                        conditions |= Q(item_6__icontains=keyword_separada)
                        conditions |= Q(item_7__icontains=keyword_separada)
                        listagem = LandingPage.objects.filter(conditions)
                        print('é listagem vazia  por palavra chave simples passando', keyword_separada)
                        return render(request, 'site/index.html', {'listagem': listagem})
    carossel_display = Carousel.objects.order_by('?')[:3]
    carossel_display_2 = Carousel.objects.order_by('?')[3:]
    print('saido docarossel_display', carossel_display)
    listagem = LandingPage.objects.all()
    carroussel_vinculado = Carousel.objects.all()
    return render(request, 'site/index.html', {'listagem': listagem,
                                               'carossel_display': carossel_display,
                                               'carossel_display_2': carossel_display_2,
                                               'carroussel_vinculado': carroussel_vinculado})


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
    carroussel_vinculado = Carousel.objects.filter(empreendimento_relacionado=nome_relacionado)
    return render(request, 'site/landing-page.html', {'empreendimento': empreendimento,
                                                      'carroussel_vinculado': carroussel_vinculado,
                                                      })


@login_required
def dashboard_lp(request):
    if request.method == 'POST':
        tipo_imovel = request.POST.get('tipo_imovel')
        status_imovel = request.POST.get('status_imovel')
        padrao_imovel = request.POST.get('padrao_imovel')
        nome_empreendimento = request.POST.get('nome_empreendimento')
        localizacao_empreendimento = request.POST.get('localizacao_empreendimento')
        logomarca_empreendimento = request.FILES.get('logo_empreendimento')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        item_1 = request.POST.get('item_adicionado_1')
        item_2 = request.POST.get('item_adicionado_2')
        item_3 = request.POST.get('item_adicionado_3')
        item_4 = request.POST.get('item_adicionado_4')
        item_5 = request.POST.get('item_adicionado_5')
        item_6 = request.POST.get('item_adicionado_6')
        item_7 = request.POST.get('item_adicionado_7')
        data_atual = datetime.now()
        user_logado = request.user.username
        print(tipo_imovel)
        LandingPage.objects.create(tipo_imovel=tipo_imovel,
                                   status_imovel=status_imovel,
                                   padrao_imovel=padrao_imovel,
                                   nome_empreendimento=nome_empreendimento,
                                   localizacao=localizacao_empreendimento,
                                   logomarca_icone=logomarca_empreendimento,
                                   data_cadastramento=data_atual,
                                   user_cadastramento=user_logado,
                                   item_1=item_1,
                                   item_2=item_2,
                                   item_3=item_3,
                                   item_4=item_4,
                                   item_5=item_5,
                                   item_6=item_6,
                                   item_7=item_7,
                                   longitude=longitude,
                                   latitude=latitude
                                   )
        lp = LandingPage.objects.last()
        return render(request, 'site/upload-img.html', {'lp': lp})
    else:
        lista_itens_destaque = ItensDestaque.objects.all()
        lista_lp = LandingPage.objects.all().order_by('-pk')
        busca = request.GET.get('barra-pesquisa')
        if busca:
            lista_lp = LandingPage.objects.filter(Q(nome_empreendimento__icontains=busca)).order_by('-pk')
        return render(request, 'site/dashboard-lp.html', {'lista_lp': lista_lp,
                                                          'busca': busca,
                                                          'lista_itens_destaque': lista_itens_destaque})


@login_required
def cadastro_lp(request, slug):
    empreendimento_relacionado = get_object_or_404(LandingPage, slug=slug)
    nome = empreendimento_relacionado.nome_empreendimento
    carousel_relacionado = Carousel.objects.filter(empreendimento_relacionado=nome)
    # print(carousel_relacionado.imagens)
    return render(request, 'site/cadastro-lp.html', {'empreendimento_relacionado': empreendimento_relacionado,
                                                     'carousel_relacionado': carousel_relacionado})


def cadastrar_lp(request):
    if request.method == 'POST':
        nome_empreendimento = request.POST.get('nome_empreendimento')
        localizacao_empreendimento = request.POST.get('localizacao_empreendimento')
        img_icone = request.FILES.get('logo_empreendimento')
        item_adicionado_1 = request.POST.get('item_adicionado-1')
        item_adicionado_2 = request.POST.get('item_adicionado-2')
        item_adicionado_3 = request.POST.get('item_adicionado-3')
        item_adicionado_4 = request.POST.get('item_adicionado-4')
        item_adicionado_5 = request.POST.get('item_adicionado-5')
        item_adicionado_6 = request.POST.get('item_adicionado-6')
        item_adicionado_7 = request.POST.get('item_adicionado-7')
        LandingPage.objects.create(nome_empreendimento=nome_empreendimento,
                                   localizacao=localizacao_empreendimento,
                                   logomarca_icone=img_icone,
                                   item_1=item_adicionado_1,
                                   item_2=item_adicionado_2,
                                   item_3=item_adicionado_3,
                                   item_4=item_adicionado_4,
                                   item_5=item_adicionado_5,
                                   item_6=item_adicionado_6,
                                   item_7=item_adicionado_7,
                                   )
        lp = LandingPage.objects.last()
        print(lp)

        return redirect(reverse('upload_img', args=[lp.nome_empreendimento]))
    else:

        return render(request, 'site/dashboard-lp.html')


def upload_img(request):
    if request.method == 'POST':
        empreendimento_vinculado = request.POST.get('empreendimento_vinculado')
        imagem = request.FILES.get('file')
        Carousel.objects.create(empreendimento_relacionado=empreendimento_vinculado, imagens=imagem)
        return render(request, 'site/dashboard-lp.html')
