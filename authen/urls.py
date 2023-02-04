from django.urls import path
from . import views

urlpatterns = [
                path('', views.HelloAuthView.as_view(), name='hello_auth'),
                path('signup/', views.UserCreationView.as_view(), name='signup'),
]