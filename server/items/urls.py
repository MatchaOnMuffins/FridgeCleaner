from django.urls import path
from .views import ItemViewSet, CategoryViewSet
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = [
    path("", views.home, name="home"),
    path("scanner", views.scanner, name="scanner"),
]

urlpatterns += router.urls
