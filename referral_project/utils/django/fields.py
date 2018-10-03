from functools import partial
from os.path import splitext, join
from typing import Type
from uuid import uuid4

from django.db.models import IntegerField, Model
from django.utils.translation import ugettext_lazy as _

from .enums import IntEnumChoices


class ActiveInactiveStatus(IntEnumChoices):
    INACTIVE = 0
    ACTIVE = 1

    class Labels:
        INACTIVE = _("Inactive")
        ACTIVE = _("Active")


ActiveInactiveStatusField = partial(
    IntegerField,
    choices=ActiveInactiveStatus.choices(),
    default=ActiveInactiveStatus.INACTIVE,
)


class ProcessStatus(IntEnumChoices):
    PENDING = 0
    COMPLETED = 1
    CANCELLED = 2

    class Labels:
        PENDING = _("Pending")
        COMPLETED = _("Completed")
        CANCELLED = _("Cancelled")


ProcessStatusField = partial(
    IntegerField,
    choices=ProcessStatus.choices(),
    default=ProcessStatus.PENDING,
)


class VerifyStatus(IntEnumChoices):
    PENDING = 0
    VERIFIED = 1
    DECLINED = 2

    class Labels:
        PENDING = _("Pending")
        VERIFIED = _("Verified")
        DECLINED = _("Declined")


VerifyStatusField = partial(
    IntegerField,
    choices=VerifyStatus.choices(),
    default=VerifyStatus.PENDING,
)


class ApproveStatus(IntEnumChoices):
    PENDING = 0
    APPROVED = 1
    DECLINED = 2

    class Labels:
        PENDING = _("Pending")
        APPROVED = _("Approved")
        DECLINED = _("Declined")


ApproveStatusField = partial(
    IntegerField,
    choices=ApproveStatus.choices(),
    default=ApproveStatus.PENDING,
)


class SubmitStatus(IntEnumChoices):
    AVAILABLE = 0
    SUBMITTED = 1

    class Labels:
        AVAILABLE = _("Available")
        SUBMITTED = _("Submitted")


SubmitStatusField = partial(
    IntegerField,
    choices=SubmitStatus.choices(),
    default=SubmitStatus.AVAILABLE,
)


def generate_upload_to(
    base_path: str,
    instance: Type[Model],
    filename: str,
):
    filename_extension = splitext(filename)[1]
    unique_filename = "{}{}".format(uuid4(), filename_extension)
    return join(base_path, unique_filename)
