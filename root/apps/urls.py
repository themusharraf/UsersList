from django.urls import path
from .views import Home, UserList

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('user_list', UserList.as_view(), name="user_list")
]
