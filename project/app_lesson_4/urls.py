from django.urls import path, include
from .views import func

urlpatterns = [
    path('', func),
]