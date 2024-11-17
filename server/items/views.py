from django.shortcuts import render

# from django.http import HttpResponse
# from django.shortcuts import render
from .models import Item
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer
from django.shortcuts import get_object_or_404


def home(request):
    items = Item.objects.all()
    return render(request, "items/home.html", {"items": items})


class ItemCreate(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetail(APIView):
    def get(self, request, uuid):
        item = get_object_or_404(Item, uuid=uuid)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    
class ItemDelete(APIView):
    def delete(self, request, uuid):
        item = get_object_or_404(Item, uuid=uuid)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ItemsList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class ItemEdit(APIView):
    def put(self, request, uuid):
        item = get_object_or_404(Item, uuid=uuid)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)