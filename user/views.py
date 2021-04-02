from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import UserListSerializer, UserDetailSerializer
from .models import User
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
