from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# It stores the trees of catgory
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    is_digital = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Category = TreeForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
