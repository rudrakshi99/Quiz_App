from accounts.models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import UserPermission

class UserListView(ListAPIView):
    serializer_class    = UserSerializer


    def get_queryset(self):
        """Returns only the object related to current user"""
        user = self.request.user
        return User.objects.filter(email=user)
    
    
class UserCreateView(CreateAPIView):
    """Handles Create of a Retailer object"""
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    permission_classes = [AllowAny]


class UserUpdateRetriveDeleteView(RetrieveUpdateDestroyAPIView):
    """Handles update, retrive and delete of retailer obj"""
    queryset            = User.objects.all()
    serializer_class    = UserSerializer

    permission_classes  = (IsAuthenticated, UserPermission)
