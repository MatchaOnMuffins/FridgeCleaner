from django.urls import path
from .views import ItemCreate, ItemsList, ItemDetail, ItemDelete, ItemEdit
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("items/", ItemsList.as_view(), name="items"),
    path("items/create/", ItemCreate.as_view(), name="item_create"),
    path("items/<uuid:uuid>/", ItemDetail.as_view(), name="item_detail"),
    path("items/<uuid:uuid>/delete/", ItemDelete.as_view(), name="item_delete"),
    path("items/<uuid:uuid>/edit/", ItemEdit.as_view(), name="item_edit"),
]
