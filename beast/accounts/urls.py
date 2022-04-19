from rest_framework import routers

from accounts import views

router = routers.DefaultRouter()
router.register('me', views.UserMeViewSet, basename="user_me")

urlpatterns = [
] + router.urls
