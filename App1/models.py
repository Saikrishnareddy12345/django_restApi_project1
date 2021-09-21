from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    starts = models.IntegerField()

    def __str__(self):
        return self.name


class Product1(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    starts = models.IntegerField()

    class Meta:
        db_table = "app1_product"

