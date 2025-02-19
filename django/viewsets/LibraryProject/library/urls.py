from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, MagazineViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'magazines', MagazineViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]