from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activity', views.ActivityViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)
router.register(r'workouts', views.WorkoutViewSet)

# The API URLs are now determined automatically by the router.
# Ensure api_root is included
urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('', include(router.urls)),
]
