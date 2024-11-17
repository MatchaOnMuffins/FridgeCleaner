from rest_framework import serializers
from .models import Item, Category



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        def create(self, validated_data):
            return Category.objects.create(**validated_data)



class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Item
        fields = "__all__"
        def create(self, validated_data):
            return Item.objects.create(**validated_data)
