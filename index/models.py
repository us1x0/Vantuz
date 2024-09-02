from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Product(models.Model):
    pr_name = models.CharField(max_length=256)
    pr_des = models.TextField(blank=True)
    pr_price = models.FloatField()
    pr_count = models.IntegerField()
    pr_photo = models.ImageField()
    pr_category = models.ForeignKey(Category, on_delete=models.CASCADE )

    def __str__(self):
        return self.pr_name

