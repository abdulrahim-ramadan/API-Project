from django.urls import path
from .views import GetAPI
urlpatterns = [
    path("",GetAPI.as_view())
]
