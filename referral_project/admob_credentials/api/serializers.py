from rest_framework.serializers import ModelSerializer

from referral_project.admob_credentials.models import AdmobCredential


class AdmobCredentialSerializer(ModelSerializer):
    class Meta:
        model = AdmobCredential
        fields = [
            'name',
            'adunittype',
            'appid',
            'adunitid',
        ]
