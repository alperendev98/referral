from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from referral_project.utils.django.admin import TimeStampedModelAdmin
from django.utils.translation import ugettext_lazy as _
from referral_project.users.models import User
from referral_project.users.models import KYC

class KYCStatusFilter(admin.SimpleListFilter):
    title = 'Has Customer'
    parameter_name = 'customer'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'YES'),
            ('no', 'NO'),
        )
    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(customer__isnull=False)
        if self.value() == 'no':
            return queryset.filter(customer__isnull=True)
        else:
            return queryset.all()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal info'), {
                'fields': (
                    'username',
                    'first_name',
                    'last_name',
                    'referrer',
                    'status',
                    'customer',
                )
            }),
        (
            _('Permissions'), {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }),
        (
            _('Important dates'), {
                'fields': (
                    'last_login',
                    'date_joined',
                )
            }
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'password1',
                'password2',
            ),
        }),
    )
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'is_staff',
        'customer'
    )
    list_filter = [
        'is_staff',
        'is_superuser',
        'is_active',
        'groups',
        KYCStatusFilter
    ]
    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name',
    )
    ordering = (
        'email',
        'username',
    )

@admin.register(KYC)
class TransactionAdmin(TimeStampedModelAdmin):
    list_display = [
        'first_name',
        'last_name',
    ]
