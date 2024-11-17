from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer
from django.shortcuts import render


def home(request):
    # render items to the home page
    items = Item.objects.all()
    return render(request, "items/home.html", {"items": items})



class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "uuid"


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "uuid"


router = DefaultRouter()
router.register(r"items", ItemViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = router.urls
