from django.db import models


# Create your models here.


class Retail(models.Model):
    pub_date = models.DateTimeField()
    items = models.TextField(blank=False, null=False)
    quantity = models.IntegerField(verbose_name=None, blank=False)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.CharField(max_length=120, default='what the item is used for?')
    phone = models.SmallIntegerField(blank=False)
    email = models.EmailField(max_length=45, null=True, blank=False)


def total_goods(quantity, price):
    return quantity * price


class Cart(models.Model):
    pub_date = models.ForeignKey(Retail, on_delete=models.CASCADE)
    total = models.IntegerField()
    # retail = models.ForeignKey(Retail.phone, on_delete=models.CASCADE)
