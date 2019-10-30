from django.db import models

# Create your models here.

class Item(models.Model): #name of the table

    type = models.CharField(max_length=100, blank=False) # name of the column
    price = models.FloatField(blank=False)
    stock = models.IntegerField(blank=False)
    item = models.CharField(max_length=100, blank=False)
    brand = models.CharField(max_length=100, blank=False)

    choices = (
        ('AMAZON', 'Amazon'),
        ('FULFILLED', 'FBA'),
        ('BAY', 'Ebay'),
        ('STOCK', 'Stock X'),
        ('GOAT', 'GOAT')
    )

    site = models.CharField(max_length=100, choices=choices, blank=False)
    purchased_price = models.FloatField(blank=False)
    posted_date = models.CharField(max_length=100, blank=False)
    bought_at = models.CharField(max_length=100, blank=False)
    model = models.CharField(max_length=100)

    class Meta:
        abstract = True


    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.type, self.price)


class Electronics(Item):
    pass

class Apparel(Item):
    type = models.CharField(max_length=100, blank=False) # name of the column
    price = models.FloatField(blank=False)
    stock = models.IntegerField(blank=False)

    choices = (
        ('AMAZON', 'Amazon'),
        ('FULFILLED', 'FBA'),
        ('BAY', 'Ebay'),
        ('STOCK', 'Stock X'),
        ('GOAT', 'GOAT')
    )

    site = models.CharField(max_length=100, choices=choices, blank=False)
    purchased_price = models.FloatField(blank=False)
    posted_date = models.CharField(max_length=100, blank=False)
    bought_at = models.CharField(max_length=100, blank=False)
    

class Equipment(Item):
    pass

class Toys(Item):
    pass

class Footwear(Item):
    type = models.CharField(max_length=100, blank=False) # name of the column
    price = models.FloatField(blank=False)
    stock = models.IntegerField(blank=False)
    item = models.CharField(max_length=100, blank=False)
    brand = models.CharField(max_length=100, blank=False)

    choices = (
        ('AMAZON', 'Amazon'),
        ('FULFILLED', 'FBA'),
        ('BAY', 'Ebay'),
        ('STOCK', 'Stock X'),
        ('GOAT', 'GOAT')
    )

    site = models.CharField(max_length=100, choices=choices, blank=False)
    purchased_price = models.FloatField(blank=False)
    posted_date = models.CharField(max_length=100, blank=False)
    bought_at = models.CharField(max_length=100, blank=False)
    model = models.CharField(max_length=100)
    shoe_size = models.IntegerField(blank=False)

