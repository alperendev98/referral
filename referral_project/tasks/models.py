from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db.models import CharField, URLField, ForeignKey, CASCADE, BooleanField, PositiveIntegerField, DateField
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from referral_project.campaigns.fields import CampaignKindField
from referral_project.campaigns.models import Campaign
from referral_project.utils.django.errors import BUSINESS_LOGIC_ERROR_CODE
from referral_project.utils.django.fields import ActiveInactiveStatusField, ActiveInactiveStatus, ApproveStatusField, ApproveStatus, SubmitStatus, SubmitStatusField
from referral_project.utils.djmoney.models.fields import ProjectMoneyField
from referral_project.wallets.fields import WalletKind
from referral_project.wallets.models import Wallet


class Task(TimeStampedModel):
    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    name = CharField(max_length=255)
    kind = CampaignKindField()
    # http://stackoverflow.com/questions/10052220/advantages-to-using-urlfield-over-textfield#comment49011703_10052288
    link = URLField(max_length=2000)
    reward = ProjectMoneyField()
    campaign = ForeignKey(
        Campaign,
        related_name='tasks',
        on_delete=CASCADE,
    )
    status = ActiveInactiveStatusField()
    max_interactions = PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name=_("Maximum allowed interactions"),
    )
    expired = BooleanField(default=False)

    def __str__(self):
        return f"{ActiveInactiveStatus(self.status).label} " \
               f"{self.reward} " \
               f"\"{self.name}\" " \
               f"(#{self.pk})"

    def interact(self, user: settings.AUTH_USER_MODEL):
        if TaskStatus.objects.filter(task=self, user=user, interacted=True).exists():
            return False
        TaskStatus.objects.create(
            task=self,
            user=user,
            interacted=True,
        )

        if self.max_interactions == self.task_status.all().count():
            self.status = ActiveInactiveStatus.INACTIVE

        wallet = Wallet.objects.filter(user=user, kind=WalletKind.MAIN).first()
        wallet.balance += self.reward
        wallet.save()
        return True

    def clean(self):
        self._validate_task_kind_matches_campaign_kind()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_clean()
        super().save(force_insert, force_update, using, update_fields)

    def _validate_task_kind_matches_campaign_kind(self):
        if self.kind != self.campaign.kind:
            raise ValidationError(
                _("Task kind must match its campaign's."),
                code=BUSINESS_LOGIC_ERROR_CODE,
            )


class TaskStatus(TimeStampedModel):  # TODO: rename to TaskInteraction
    class Meta:
        verbose_name = _("Task Status")
        verbose_name_plural = _("Task Statuses")

    interacted = BooleanField(default=False)  # TODO: remove as mere existence of the model indicates truthfulness
    user_ip = CharField(
        max_length=45,
        blank=True,
        null=True
    )
    date = DateField(
        blank=True,
        null=True
    )
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='interacted_tasks',  # TODO: rename related_name='interactions'
        on_delete=CASCADE,
    )
    task = ForeignKey(
        Task,
        related_name='task_status',  # TODO: rename related_name='interactions'
        on_delete=CASCADE,
    )
    parent_campaign = ForeignKey(
        Campaign,
        blank=True,
        null=True,
        on_delete=CASCADE
    )

    def __str__(self):
        return f"#{self.user_id} " \
               f"{'interacted' if self.interacted else 'did not interact'} " \
               f"with #{self.task_id} " \
               f"(#{self.pk})"

    def clean(self):
        self._validate_task_not_expired()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_clean()
        super().save(force_insert, force_update, using, update_fields)

    def _validate_task_not_expired(self):
        if self.task.expired:
            raise ValidationError(
                _("Task #%(task_id)s expired."),
                code=BUSINESS_LOGIC_ERROR_CODE,
                params={'task_id': self.task_id},
            )


class CustomTask(TimeStampedModel):
    class Meta:
        verbose_name = _("Custom Task")
        verbose_name_plural = _("Custom Tasks")

    title = CharField(max_length=255)
    reward = ProjectMoneyField()
    instruction = CharField(max_length=2000)
    campaign = ForeignKey(
        Campaign,
        related_name='custom_tasks',
        on_delete=CASCADE,
    )
    status = ApproveStatusField()
    max_interactions = PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name=_("Maximum allowed interactions"),
    )
    expired = BooleanField(default=False)
    work_proof = CharField(
        max_length=255,
        null=True,
        blank=True
    )
    action = SubmitStatusField()

    def __str__(self):
        return f"{ApproveStatus(self.status).label} " \
               f"{self.reward} " \
               f"\"{self.title}\" " \
               f"(#{self.pk})"

    def interact(self, user: settings.AUTH_USER_MODEL):
        if CustomTaskStatus.objects.filter(task=self, user=user).exists():
            return False
        CustomTaskStatus.objects.create(
            task=self,
            user=user,
        )

        if self.max_interactions == self.custom_task_status.all().count():
            self.status = ActiveInactiveStatus.INACTIVE

        wallet = Wallet.objects.filter(user=user, kind=WalletKind.MAIN).first()
        wallet.balance += self.reward
        wallet.save()
        return True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_clean()
        super().save(force_insert, force_update, using, update_fields)


class CustomTaskStatus(TimeStampedModel):  # TODO: rename to TaskInteraction
    class Meta:
        verbose_name = _("Custom Task Status")
        verbose_name_plural = _("Custom Task Statuses")

    interacted = BooleanField(default=False)  # TODO: remove as mere existence of the model indicates truthfulness
    user_ip = CharField(
        max_length=45,
        blank=True,
        null=True
    )
    date = DateField(
        blank=True,
        null=True
    )
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='custom_interacted_tasks',  # TODO: rename related_name='interactions'
        on_delete=CASCADE,
    )
    task = ForeignKey(
        CustomTask,
        related_name='custom_task_status',  # TODO: rename related_name='interactions'
        on_delete=CASCADE,
    )
    parent_campaign = ForeignKey(
        Campaign,
        blank=True,
        null=True,
        on_delete=CASCADE
    )

    def __str__(self):
        return f"#{self.user_id} " \
               f"{'interacted' if self.interacted else 'did not interact'} " \
               f"with #{self.task_id} " \
               f"(#{self.pk})"

    def clean(self):
        self._validate_task_not_expired()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_clean()
        super().save(force_insert, force_update, using, update_fields)

    def _validate_task_not_expired(self):
        if self.task.expired:
            raise ValidationError(
                _("Task #%(task_id)s expired."),
                code=BUSINESS_LOGIC_ERROR_CODE,
                params={'task_id': self.task_id},
            )
