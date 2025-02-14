from django.db import models
import uuid


class Category(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    good_for = models.IntegerField()

    def __str__(self):
        return self.name

class Item(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
