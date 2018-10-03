from django.db import models

# Create your models here.
from django.db.models import CASCADE, ForeignKey, CharField
from referral_project.admob_credentials.fields import AdmobTypeOptionField, AdmobTypeOption
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

class AdmobCredential(TimeStampedModel):
    class Meta:
        verbose_name = _("AdmobCredential")
        verbose_name_plural = _("AdmobCredentials")

    name = CharField(max_length=30, null=True, verbose_name='Ad unit name')
    appid = CharField(max_length=30, null=True, verbose_name='App id')
    adunitid = CharField(max_length=30, null=True, verbose_name='Ad unit id')
    adunittype = AdmobTypeOptionField(verbose_name='Ad unit type')

    def __str__(self):
        return f"{self.name} " \
               f" for {AdmobTypeOptionField(self.adunittype)} " \
