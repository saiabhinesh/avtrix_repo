from django.db import models

# Create your models here.

class Order(models.Model):
    OrderDate = models.DateTimeField()
    Region = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    Product = models.CharField(max_length=50)
    Quantity = models.IntegerField()
    UnitPrice = models.FloatField()

    class Meta:
        db_table = 'FoodSales'
    
    def __str__(self) -> str:
        return self.Product