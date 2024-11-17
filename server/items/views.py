from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer
from django.shortcuts import render
from datetime import date, timedelta
import json
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse


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

@csrf_exempt
def update_item(request, uuid):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item = Item.objects.get(uuid=uuid)

            # Update the item with the new data, validating dates
            item.name = data.get('name', item.name)
            
            # Check for valid purchase_date and fridge_date
            purchase_date = data.get('purchase_date')
            fridge_date = data.get('fridge_date')
            
            if purchase_date:
                item.purchase_date = purchase_date  # Must be in YYYY-MM-DD format
            if fridge_date:
                item.fridge_date = fridge_date  # Must be in YYYY-MM-DD format
            
            item.save()

            return JsonResponse({'status': 'success', 'message': 'Item updated successfully.'})
        except Item.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Item not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

router = DefaultRouter()
router.register(r"items", ItemViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = router.urls
