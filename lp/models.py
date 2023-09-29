from django.db import models
from django.template.defaultfilters import slugify  # new
from django.urls import reverse
from django_resized import ResizedImageField


# Create your models here.

class Leads(models.Model):
    nome_leads = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=13)
    status_aberto = models.CharField(max_length=20)
    status_leads = models.CharField(max_length=8)
    data_recebimento = models.CharField(max_length=50)
    ultimo_user = models.CharField(max_length=30)

    def __str__(self):
        return self.nome_leads


class LandingPage(models.Model):
    padrao_imovel = models.CharField(max_length=30, blank=False, null=False)
    status_imovel = models.CharField(max_length=30, blank=False, null=False)
    tipo_imovel = models.CharField(max_length=30, blank=False, null=False)
    nome_construtora = models.CharField(max_length=100, blank=True, null=True)
    nome_empreendimento = models.CharField(max_length=100, blank=False, null=False)
    endereco_empreendimento = models.CharField(max_length=300, blank=True, null=True)
    bairro = models.CharField(max_length=300, blank=True, null=True)
    area_construida = models.CharField(max_length=10, blank=False, null=False)
    qtde_quartos = models.CharField(max_length=10, blank=True, null=True)
    qtde_suites = models.CharField(max_length=10, blank=True, null=True)
    qtde_vaga_garagem = models.CharField(max_length=20, blank=True, null=True)
    item_opcional_1 = models.CharField(max_length=30, blank=True, null=True)
    item_opcional_2 = models.CharField(max_length=30, blank=True, null=True)
    item_opcional_3 = models.CharField(max_length=30, blank=True, null=True)
    item_opcional_4 = models.CharField(max_length=30, blank=True, null=True)
    item_opcional_5 = models.CharField(max_length=30, blank=True, null=True)
    item_opcional_6 = models.CharField(max_length=30, blank=True, null=True)
    item_opcional_7 = models.CharField(max_length=30, blank=True, null=True)
    item_opcional_8 = models.CharField(max_length=30, blank=True, null=True)
    item_opcional_9 = models.CharField(max_length=30, blank=True, null=True)
    item_opcional_10 = models.CharField(max_length=30, blank=True, null=True)
    info_complementares = models.TextField(max_length=1000, blank=True, null=True)
    anunciado_por = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
    imagem_1 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                 null=True)
    imagem_2 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                 null=True)
    imagem_3 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                 null=True)
    imagem_4 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                 null=True)
    imagem_5 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                 null=True)
    imagem_6 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                 null=True)
    imagem_7 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                 null=True)
    imagem_8 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                 null=True)
    imagem_9 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                 null=True)
    imagem_10 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                  null=True)
    imagem_11 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                  null=True)
    imagem_12 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                  null=True)
    imagem_13 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                  null=True)
    imagem_14 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                  null=True)
    imagem_15 = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                  null=True)

    def __str__(self):
        combined_string = f"{self.tipo_imovel}/{self.nome_empreendimento}"
        return combined_string

    def get_absolute_url(self):
        return reverse("landingpage", kwargs={"slug": self.slug})

    from django.utils.text import slugify

    def save(self, *args, **kwargs):
        if not self.slug:
            combined_string = f"{self.tipo_imovel}-{self.nome_empreendimento}"
            self.slug = slugify(combined_string)
        return super().save(*args, **kwargs)


class Cores(models.Model):
    nome_cor = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_cor


class ItensOpcioanis(models.Model):
    nome_item = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_item


class QtdeQuartos(models.Model):
    qtde_quartos = models.CharField(max_length=100)

    def __str__(self):
        return self.qtde_quartos


class Qtdesuites(models.Model):
    qtde_suites = models.CharField(max_length=100)

    def __str__(self):
        return self.qtde_suites


class QtdeVagaGaragem(models.Model):
    qtde_vagas_garagem = models.CharField(max_length=100)

    def __str__(self):
        return self.qtde_vagas_garagem


class Perfil(models.Model):
    user_vinculado = models.CharField(max_length=50)
    whatsa_app = models.CharField(max_length=15)
    perfil_facebook = models.TextField(max_length=1000, null=True, blank=True)
    perfil_instagram = models.TextField(max_length=1000, null=True, blank=True)
    img_perfil = ResizedImageField(size=[150, 150], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                   null=True)

    def __str__(self):
        return self.user_vinculado


class Tagmeta(models.Model):
    editado_por = models.CharField(max_length=50)
    data_atualizacao = models.CharField(max_length=15)
    tag_meta = models.TextField(max_length=256)


class TagGoogle(models.Model):
    editado_por = models.CharField(max_length=50)
    data_atualizacao = models.CharField(max_length=15)
    tag_google = models.TextField()


class TagGoogleBody(models.Model):
    editado_por = models.CharField(max_length=50)
    data_atualizacao = models.CharField(max_length=15)
    tag_google_body = models.TextField(max_length=256)
