from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Leads, Perfil, Tagmeta, TagGoogle, LandingPage, ItensDestaque
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q

# Create your views here.

# Substitua "SUA_CHAVE_DE_API" pela sua chave de API do Google Maps
chave = "AIzaSyA6EVGvxZFbZ1wg_5pP9onIn9FQeh1VBFY"


def index(request):
    return render(request, 'site/index.html')


def abrirleads(request, pk):
    status_aberto = 'fa-envelope-open'
    Leads.objects.filter(pk=pk).update(status_aberto=status_aberto)


@login_required
def dashboard(request):
    leads = Leads.objects.all().order_by('-data_recebimento')
    leads_novos = Leads.objects.filter(status_aberto='fa-envelope')
    leads_abertos = Leads.objects.filter(status_aberto='fa-envelope-open')
    perfil_user = Perfil.objects.last()
    return render(request, 'site/dashboard.html', {'leads': leads,
                                                   'perfil_user': perfil_user,
                                                   'leads_novos': leads_novos,
                                                   'leads_abertos': leads_abertos})


def estoque_veiculos(request):
    veiculo = LandingPage.objects.all()
    busca = request.GET.get('barra-pesquisa')
    if busca:
        veiculo = LandingPage.objects.filter(
            Q(nome_modelo__icontains=busca) | Q(nome_marca__icontains=busca) | Q(ano__icontains=busca) | Q(
                combustivel__icontains=busca) | Q(cambio__icontains=busca) | Q(
                cor__icontains=busca) | Q(portas__icontains=busca)
        )

    return render(request, 'site/dashboard-gerenciador-estoque.html', {'veiculo': veiculo})


def deletar_lp(request, pk):
    if request.method == "POST":
        lp = LandingPage.objects.filter(pk=pk)
        print(lp)
        lp.delete()
        return redirect('estoque-veiculos')


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


def abrirleads(request, pk):
    status_aberto = 'fa-envelope-open'
    Leads.objects.filter(pk=pk).update(status_aberto=status_aberto)


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


def landingpage(request, pk, slug):
    if request.method == 'POST':
        nome_leads = request.POST.get('nome_leads')
        whatsapp_leads = request.POST.get('whatsapp_leads')
        recebido_em = datetime.now()
        Leads.objects.create(nome_leads=nome_leads,
                             whatsapp=whatsapp_leads,
                             data_recebimento=recebido_em)
        return render(request, 'site/landingpage.html', {'veiculo': veiculo})
    veiculo = get_object_or_404(LandingPage, pk=pk, slug=slug)
    return render(request, 'site/landingpage.html', {'veiculo': veiculo})


@login_required
def dashboard_lp(request):
    if request.method == 'POST':
        marca = request.POST.get('field-marca')
        modelo = request.POST.get('field-modelo')
        ano = request.POST.get('field-ano')
        combustivel = request.POST.get('combustivel')
        cor = request.POST.get('cor')
        portas = request.POST.get('portas')
        cambio = request.POST.get('cambio')
        ipva = request.POST.get('ipva')
        placa = request.POST.get('placa')
        valor = request.POST.get('valor')
        acendedor_cigarros = request.POST.get('acendedor_cigarros')
        air_bags = request.POST.get('air_bags')
        alarme = request.POST.get('alarme')
        ar_condicionado = request.POST.get('ar_condicionado')
        ar_condicionado_digital = request.POST.get('ar_condicionado_digital')
        ar_condicionado_dual_zone = request.POST.get('ar_condicionado_dual_zone')
        ar_quente = request.POST.get('ar_quente')
        assistente_saida_aclive = request.POST.get('assistente_saida_aclive')
        sistema_audio = request.POST.get('sistema audio')
        banco_apoio_braco = request.POST.get('banco_apoio_banco')
        banco_regulagem_eletrica = request.POST.get('banco_regulagem_eletrica')
        blindado = request.POST.get('blindado')
        bluetooth = request.POST.get('bluetooth')
        calotas = request.POST.get('calotas')
        camera_re = request.POST.get('camera_re')
        carregador_dispositivo_wireless = request.POST.get('carregador_dispositivo_wireless')
        cd_mp3 = request.POST.get('cd_mp3')
        chaves_keyless = request.POST.get('chaves_keyless')
        chaves_sensor_presenca = request.POST.get('chaves_sensor_presenca')
        computador_bordo = request.POST.get('computador_bordo')
        controle_som_volante = request.POST.get('controle_som_volante')
        controle_eletronico_descida = request.POST.get('controle_eletronico_descida')
        desembacador_traseiro = request.POST.get('desembacador_traseiro')
        direcao_eletrica = request.POST.get('direcao_eletrica')
        direcao_hidraulica = request.POST.get('direcao_hidraulica')
        encosto_cabeca_traseiro = request.POST.get('encosto_cabeca_traseiro')
        estribo = request.POST.get('estribo')
        farois_automatico = request.POST.get('farois_automatico')
        farois_milhas = request.POST.get('farois_milhas')
        farois_neblina = request.POST.get('farois_neblina')
        freio_abs = request.POST.get('freio_abs')
        gps = request.POST.get('gps')
        insulfilm = request.POST.get('insulfilm')
        lona_maritima = request.POST.get('lona_maritima')
        multimidia = request.POST.get('multimidia')
        painel_lcd = request.POST.get('painel_lcd')
        painel_digital = request.POST.get('paienl_digital')
        parachoque_cor_veiculo = request.POST.get('parachoque_cor_veiculo')
        park_assist = request.POST.get('park_assist')
        partida_start_stop = request.POST.get('partida_start_stop')
        piloto_automatico = request.POST.get('piloto_automatico')
        pintura_metalica = request.POST.get('pintura_metalica')
        porta_copo = request.POST.get('porta_copo')
        protecao_cacamba = request.POST.get('protecao_cacamba')
        radio = request.POST.get('radio')
        rebatimento_retrovisores_externos = request.POST.get('rebatimento_retrovisores_externos')
        retrovisor_fotocromatico = request.POST.get('retrovisor_fotocromatico')
        retrovisor_interno_eletrocromico = request.POST.get('retrovisor_interno_eletrocromico')
        retrovisor_eletrico = request.POST.get('retrovisor_eletrico')
        roda_liga_leve = request.POST.get('roda_liga_leve')
        sensor_chuva = request.POST.get('sensor_chuva')
        sensor_estacionamento_dianteiro = request.POST.get('sensor_estacionamento_dianteiro')
        sensor_estacionamento_traseiro = request.POST.get('sensor_estacionamento_traseiro')
        teto_solar = request.POST.get('teto_solar')
        teto_panoramico = request.POST.get('teto_panoramico')
        tracao = request.POST.get('tracao')
        trava_eletrica = request.POST.get('trava_eletrica')
        usb = request.POST.get('usb')
        vidro_eletrico = request.POST.get('vidro_eletrico')
        vidro_verdes = request.POST.get('vidro_verdes')
        volante_regulagem_altura = request.POST.get('volante_regulagem_altura')
        anunciado_por = request.user
        LandingPage.objects.create(nome_modelo=modelo,
                                   nome_marca=marca,
                                   combustivel=combustivel,
                                   cor=cor,
                                   ano=ano,
                                   portas=portas,
                                   cambio=cambio,
                                   ipva=ipva,
                                   placa=placa,
                                   valor=valor,
                                   acendedor_cigarros=acendedor_cigarros,
                                   air_bags=air_bags,
                                   alarme=alarme,
                                   ar_condicionado=ar_condicionado,
                                   ar_condicionado_digital=ar_condicionado_digital,
                                   ar_condicionado_dual_zone=ar_condicionado_dual_zone,
                                   ar_quente=ar_quente,
                                   assistente_saida_aclive=assistente_saida_aclive,
                                   sistema_audio=sistema_audio,
                                   banco_apoio_braco=banco_apoio_braco,
                                   banco_regulagem_eletrica=banco_regulagem_eletrica,
                                   blindado=blindado,
                                   bluetooth=bluetooth,
                                   calotas=calotas,
                                   camera_re=camera_re,
                                   carregador_dispositivo_wireless=carregador_dispositivo_wireless,
                                   cd_mp3=cd_mp3,
                                   chaves_keyless=chaves_keyless,
                                   chaves_sensor_presenca=chaves_sensor_presenca,
                                   computador_bordo=computador_bordo,
                                   controle_eletronico_descida=controle_eletronico_descida,
                                   controle_som_volante=controle_som_volante,
                                   desembacador_traseiro=desembacador_traseiro,
                                   direcao_eletrica=direcao_eletrica,
                                   direcao_hidraulica=direcao_hidraulica,
                                   encosto_cabeca_traseiro=encosto_cabeca_traseiro,
                                   estribo=estribo,
                                   farois_automatico=farois_automatico,
                                   farois_milhas=farois_milhas,
                                   farois_neblina=farois_neblina,
                                   freio_abs=freio_abs,
                                   gps=gps,
                                   insulfilm=insulfilm,
                                   lona_maritima=lona_maritima,
                                   multimidia=multimidia,
                                   painel_lcd=painel_lcd,
                                   painel_digital=painel_digital,
                                   parachoque_cor_veiculo=parachoque_cor_veiculo,
                                   park_assist=park_assist,
                                   partida_start_stop=partida_start_stop,
                                   piloto_automatico=piloto_automatico,
                                   pintura_metalica=pintura_metalica,
                                   porta_copo=porta_copo,
                                   protecao_cacamba=protecao_cacamba,
                                   radio=radio,
                                   rebatimento_retrovisores_externos=rebatimento_retrovisores_externos,
                                   retrovisor_fotocromatico=retrovisor_fotocromatico,
                                   retrovisor_interno_eletrocromico=retrovisor_interno_eletrocromico,
                                   retrovisor_eletrico=retrovisor_eletrico,
                                   roda_liga_leve=roda_liga_leve,
                                   sensor_chuva=sensor_chuva,
                                   sensor_estacionamento_dianteiro=sensor_estacionamento_dianteiro,
                                   sensor_estacionamento_traseiro=sensor_estacionamento_traseiro,
                                   teto_solar=teto_solar,
                                   teto_panoramico=teto_panoramico,
                                   tracao=tracao,
                                   trava_eletrica=trava_eletrica,
                                   usb=usb,
                                   vidro_eletrico=vidro_eletrico,
                                   vidro_verdes=vidro_verdes,
                                   volante_regulagem_altura=volante_regulagem_altura,
                                   anunciado_por=anunciado_por)
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
        veiculo_vinculado = request.POST.get('veiculo_vinculado')
        # Obtém a instância do objeto LandingPage ou retorna 404 se não existir
        landing_page = get_object_or_404(LandingPage, pk=veiculo_vinculado)
        print('lp é', landing_page)

        # Obtém as imagens enviadas através do campo 'file' no formulário
        imagens = request.FILES.getlist('file')

        # Lógica para salvar as imagens na instância do objeto LandingPage
        for idx, img in enumerate(imagens, start=1):
            if idx <= 10:  # Certifique-se de que não estamos excedendo o número máximo de imagens
                image_field = 'imagem_' + str(idx)
                landing_page.image_field = img
                setattr(landing_page, image_field, img)
        # Salva o objeto LandingPage no banco de dados após adicionar as imagens
        landing_page.save()

        return render(request, 'site/dashboard-lp.html')
