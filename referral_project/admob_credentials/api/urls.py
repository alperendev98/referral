from rest_framework.routers import DefaultRouter

from referral_project.admob_credentials.api.views import AdmobCredentials

router = DefaultRouter()

router.register(r'admob_credentials', AdmobCredentials, base_name='AdmobCredentials')

urlpatterns = router.urls