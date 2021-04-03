from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import UserListSerializer, UserDetailSerializer
from .models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwner


class UserViewSet(ModelViewSet):

    def get_permissions(self):
        if self.action in ['list', 'get']:
            self.permission_classes = [IsAuthenticated, ]
        elif self.action in ['put', 'update']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        if self.request.user.pk == User.pk:
            return User.objects.filter(user__id=self.request.user.pk)
        else:
            return User.objects.all()

    def get_serializer_class(self):
        if self.action == 'put' or self.action == 'update':
            return UserListSerializer
        else:
            return UserDetailSerializer


