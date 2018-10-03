from rest_framework.decorators import detail_route
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework import viewsets, mixins
from django.conf import settings
from referral_project.tasks.api.v0.serializers import TaskSerializer, CustomTaskSerializer
from referral_project.tasks.models import Task, CustomTask
from referral_project.users.fields import ActivatedDeactivatedStatus
from referral_project.utils.django.fields import ActiveInactiveStatus
from constance import config


class Tasks(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.action == 'list':
            user = self.request.user
            queryset = Task.objects.filter(
                expired=False,
                status=ActiveInactiveStatus.ACTIVE
            ).exclude(
                task_status__user=user,
                task_status__interacted=True,
            )
            filter = self.request.GET.get('kind', None)
            if filter is not None:
                queryset = queryset.filter(kind=int(filter))

            if user.status == ActivatedDeactivatedStatus.ACTIVATED:
                queryset = queryset[:config.PAID_MIN_DAILY_VIDEO]
            else:
                queryset = queryset[:config.FREE_MIN_DAILY_VIDEO]
        else:
            queryset = Task.objects.all()
        return queryset

    @detail_route(methods=['post'])
    def interact(self, request: Request, pk: int = None) -> Response:
        authenticated_user = request.user
        task = self.get_object()

        if task.interact(authenticated_user):
            return Response({'message': 'Successfully Interacted'}, status=HTTP_200_OK)
        else:
            return Response({'message': 'You are already Interacted'}, status=HTTP_200_OK)


class CustomTasks(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CustomTaskSerializer

    def get_queryset(self):
        if self.action == 'list':
            user = self.request.user
            queryset = CustomTask.objects.filter(
                expired=False,
                status=ActiveInactiveStatus.ACTIVE
            ).exclude(
                task_status__user=user,
            )

            if user.status == ActivatedDeactivatedStatus.ACTIVATED:
                queryset = queryset[:config.PAID_MIN_DAILY_VIDEO]
            else:
                queryset = queryset[:config.FREE_MIN_DAILY_VIDEO]
        else:
            queryset = Task.objects.all()
        return queryset

    @detail_route(methods=['post'])
    def interact(self, request: Request, pk: int = None) -> Response:
        authenticated_user = request.user
        task = self.get_object()

        if task.interact(authenticated_user):
            return Response({'message': 'Successfully Interacted'}, status=HTTP_200_OK)
        else:
            return Response({'message': 'You are already Interacted'}, status=HTTP_200_OK)
