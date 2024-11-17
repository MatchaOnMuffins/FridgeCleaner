from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter

from .forms import ItemForm
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer
from django.shortcuts import render
from datetime import date, timedelta

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def home(request):
    items = Item.objects.select_related("category").all()
    today = date.today()

    for item in items:
        good_for_days = timedelta(days=item.category.good_for)
        degraded_threshold = timedelta(days=item.category.good_for * 0.75)
        expiration_date = item.purchase_date + good_for_days

        days_difference = (expiration_date - today).days
        if days_difference >= 0:
            item.days_remaining = days_difference
        else:
            item.days_remaining = abs(days_difference)

        if expiration_date < today:
            item.status = "Expired"
        elif item.purchase_date + degraded_threshold < today:
            item.status = "Degraded"
        else:
            item.status = "Fresh"

    return render(request, "items/home.html", {"items": items, "today": today})


def scanner(request):
    return render(request, "items/scanner.html")


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "uuid"


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "uuid"



class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    # fields = ['name', 'category', 'purchase_date', 'notes']  # Include the fields you want to display
    template_name = 'items/upload.html'  # Custom template for the form
    success_url = reverse_lazy('home')  # Redirect after successful creation



class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'good_for']
    template_name = 'items/new_category.html'
    success_url = reverse_lazy('item_create')  # Redirect back to the item creation page

router = DefaultRouter()
router.register(r"items", ItemViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = router.urls
