from rest_framework import viewsets, mixins
from referral_project.admob_credentials.api.serializers import AdmobCredentialSerializer
from referral_project.admob_credentials.models import AdmobCredential
from referral_project.admob_credentials.fields import AdmobTypeOption


class AdmobCredentials(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = AdmobCredentialSerializer

    def get_queryset(self):

        filter = self.request.GET.get('type', None)
        if filter == 'banner':
            return AdmobCredential.objects.filter(adunittype=AdmobTypeOption.BANNER)
        if filter == 'interstitial':
            return AdmobCredential.objects.filter(adunittype=AdmobTypeOption.INTERSTITIAL)
        if filter == 'rewards':
          return AdmobCredential.objects.filter(adunittype=AdmobTypeOption.REWARDS)
        else:
            return AdmobCredential.objects.all()
