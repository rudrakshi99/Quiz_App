from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserCreateView, UserListView, UserUpdateRetriveDeleteView

app_name='accounts'

urlpatterns = [
    
    path('users/profile/', UserListView.as_view()),
    path('users/<int:pk>', UserUpdateRetriveDeleteView.as_view()),
    path('register/', UserCreateView.as_view()),
    path('login/', obtain_auth_token)

]
    