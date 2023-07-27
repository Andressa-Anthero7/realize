from django.db import models
from django.template.defaultfilters import slugify  # new
from django.urls import reverse
from django_resized import ResizedImageField


# Create your models here.

class Leads(models.Model):
    nome_leads = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=13)
    status_aberto = models.CharField(max_length=20)
    status_leads = models.CharField(max_length=8)
    data_recebimento = models.CharField(max_length=50)
    ultimo_user = models.CharField(max_length=30)


class LandingPage(models.Model):
    tipo_imovel = models.CharField(max_length=15,null=False, blank=False)
    status_imovel = models.CharField(max_length=20,null=False, blank=False)
    padrao_imovel = models.CharField(max_length=30,null=False, blank=False)
    nome_empreendimento = models.CharField(max_length=50,null=False, blank=False)
    localizacao = models.CharField(max_length=256,null=False, blank=False)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    logomarca_icone = ResizedImageField(size=[50, 50], quality=100, upload_to='media/', force_format='PNG')
    tag_meta = models.CharField(max_length=256)
    tag_google = models.CharField(max_length=256)
    user_cadastramento = models.CharField(max_length=50)
    data_cadastramento = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True)
    item_1 = models.CharField(max_length=200, null=True, blank=True)
    item_2 = models.CharField(max_length=200, null=True, blank=True)
    item_3 = models.CharField(max_length=200, null=True, blank=True)
    item_4 = models.CharField(max_length=200, null=True, blank=True)
    item_5 = models.CharField(max_length=200, null=True, blank=True)
    item_6 = models.CharField(max_length=200, null=True, blank=True)
    item_7 = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.nome_empreendimento

    def get_absolute_url(self):
        return reverse("landingpage", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.nome_empreendimento)
        return super().save(*args, **kwargs)


class Carousel(models.Model):
    empreendimento_relacionado = models.CharField(max_length=50)
    imagens = ResizedImageField(size=[1440, 480], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                null=True)

    def __str__(self):
        return self.empreendimento_relacionado


class Perfil(models.Model):
    user_vinculado = models.CharField(max_length=50)
    img_perfil = ResizedImageField(size=[150, 150], quality=100, upload_to='media/', force_format='PNG', blank=True,
                                   null=True)


class Tagmeta(models.Model):
    editado_por = models.CharField(max_length=50)
    data_atualizacao = models.CharField(max_length=15)
    tag_meta = models.CharField(max_length=256)


class TagGoogle(models.Model):
    editado_por = models.CharField(max_length=50)
    data_atualizacao = models.CharField(max_length=15)
    tag_google = models.CharField(max_length=256)


class ItensDestaque(models.Model):
    item_cadastrado = models.CharField(max_length=100)

    def __str__(self):
        return self.item_cadastrado
