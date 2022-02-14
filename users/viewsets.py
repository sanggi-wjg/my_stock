from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, mixins, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from common.permissions import IsOwnerOrReadOnly
from users.serializers import UserSerializer, GroupSerializer


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetailViewSet(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        # mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail = True, renderer_classes = [renderers.StaticHTMLRenderer])
    def html(self, request, *args, **kwargs):
        group: 'Group' = self.get_object()
        return Response(group.name)
