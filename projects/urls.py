from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CertificateViewSet,
    CertifyingInstitutionViewSet,
    ProfileViewSet,
    ProjectViewSet,
)

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
