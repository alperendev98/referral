from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class AdmobCredentialConfig(AppConfig):
    name = 'referral_project.admob_credentials'
    verbose_name = _("AdmobCredential")

    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import signals  # noqa
