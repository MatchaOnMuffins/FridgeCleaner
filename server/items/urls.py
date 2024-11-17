from django.urls import path
from .views import ItemCreateView, ItemViewSet, CategoryViewSet, CategoryCreateView
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"items", ItemViewSet, basename="item")
router.register(r"categories", CategoryViewSet, basename="category")


urlpatterns = [
    path("", views.home, name="home"),
    path("scanner", views.scanner, name="scanner"),
    path("item/new/", ItemCreateView.as_view(), name="item_create"),
    path("category/new/", CategoryCreateView.as_view(), name="category_create"),
]

urlpatterns += router.urls
