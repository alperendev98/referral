from rest_framework.serializers import ModelSerializer

from referral_project.tasks.models import Task, CustomTask


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'kind',
            'link',
            'reward',
            'campaign',
            'status',
            'max_interactions',
            'expired',
        ]

class CustomTaskSerializer(ModelSerializer):
    class Meta:
        model = CustomTask
        fields = [
            'id',
            'title',
            'reward',
            'instruction',
            'campaign',
            'status',
            'max_interactions',
            'expired',
            'work_proof',
            'action',
        ]
