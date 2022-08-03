from django.urls import path
from clients.views import lobby

urlpatterns = [
    path('', lobby, name='lobby')
]
