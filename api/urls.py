from django.urls import path, include
from rest_framework import routers
from api.views import AnimeViewSet

router = routers.DefaultRouter()
router.register('animes', AnimeViewSet, basename='Animes')

urlpatterns = [
    path('', include(router.urls))
]
