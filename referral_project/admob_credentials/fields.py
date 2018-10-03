from functools import partial

from django.db.models import IntegerField
from django.utils.translation import ugettext_lazy as _

from referral_project.utils.django.enums import IntEnumChoices


class AdmobTypeOption(IntEnumChoices):
    BANNER = 0
    INTERSTITIAL = 1
    REWARDS = 2

    class Labels:
        BANNER = _("Banner")
        INTERSTITIAL = _("Interstitial")
        REWARDS = _("Rewards")


AdmobTypeOptionField = partial(
    IntegerField,
    choices=AdmobTypeOption.choices(),
    default=AdmobTypeOption.BANNER
)
