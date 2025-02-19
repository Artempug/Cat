from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpyCatViewSet, MissionViewSet, TargetViewSet

#Create a router for API URL routing
router = DefaultRouter()
router.register(r'spycats', SpyCatViewSet)  #Route for SpyCatViewSet
router.register(r'missions', MissionViewSet)  #Route for MissionViewSet
router.register(r'targets', TargetViewSet)  #Route for TargetViewSet

# URL patterns for the application
urlpatterns = [
    path('', include(router.urls)),  #Include router URLs
]
