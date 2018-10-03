from django.contrib import admin

from referral_project.utils.django.admin import TimeStampedModelAdmin
from referral_project.admob_credentials.models import AdmobCredential


@admin.register(AdmobCredential)
class AdmobCredentialAdmin(TimeStampedModelAdmin):
    list_display = [
        'name',
        'adunittype',
        'appid',
        'adunitid',
    ]
    list_filter = [
        'adunittype',
    ]
