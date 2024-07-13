from django.urls import path
from .views import RegisterAPIView, LoginAPIView, MainFormAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('mainform/', MainFormAPIView.as_view(), name='mainform'),
]
