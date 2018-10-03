from rest_framework.routers import DefaultRouter

from referral_project.tasks.api.v0.views import Tasks, CustomTasks

router = DefaultRouter()

router.register(r'tasks', Tasks, base_name='Tasks')
router.register(r'custom_tasks', CustomTasks, base_name='CustomTasks')

urlpatterns = router.urls
