from rest_framework.serializers import ModelSerializer

from referral_project.campaigns.models import Campaign


class CampaignSerializer(ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'id',
            'name',
            'kind',
            'started_at',
            'finished_at',
            'prototype',
            'budget',
            'status',
            'enable_for_paid_user',
            'enable_for_free_user',
            'pre_url',
        ]
