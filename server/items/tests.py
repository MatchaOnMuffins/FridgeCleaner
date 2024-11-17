from django.test import TestCase
from .models import Item, Category


class ItemCreateTest(TestCase):
    def test_create_item(self):
        category = Category.objects.create(name="Fruit")
        item = Item.objects.create(
            name="Apple",
            category=category,
            purchase_date="2021-06-01",
            fridge_date="2021-06-10",
            status="Fresh",
        )
        self.assertEqual(item.name, "Apple")
        self.assertEqual(item.category, category)
        self.assertEqual(item.purchase_date, "2021-06-01")
        self.assertEqual(item.fridge_date, "2021-06-10")
        self.assertEqual(item.status, "Fresh")

    def test_create_category(self):
        category = Category.objects.create(name="Fruit")
        self.assertEqual(category.name, "Fruit")


class ItemDeleteTest(TestCase):
    def test_delete_item(self):
        category = Category.objects.create(name="Fruit")
        item = Item.objects.create(
            name="Apple",
            category=category,
            purchase_date="2021-06-01",
            fridge_date="2021-06-10",
            status="Fresh",
        )
        item.delete()
        self.assertEqual(Item.objects.count(), 0)


class ItemEditTest(TestCase):
    def test_edit_item(self):
        category = Category.objects.create(name="Fruit")
        item = Item.objects.create(
            name="Apple",
            category=category,
            purchase_date="2021-06-01",
            fridge_date="2021-06-10",
            status="Fresh",
        )
        item.name = "Banana"
        item.save()
        self.assertEqual(item.name, "Banana")


class ItemDetailTest(TestCase):
    def test_retrieve_item(self):
        category = Category.objects.create(name="Fruit")
        item = Item.objects.create(
            name="Apple",
            category=category,
            purchase_date="2021-06-01",
            fridge_date="2021-06-10",
            status="Fresh",
        )
        retrieved_item = Item.objects.get(uuid=item.uuid)
        self.assertEqual(retrieved_item, item)