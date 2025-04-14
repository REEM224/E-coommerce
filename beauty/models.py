from django.db import models

# Create your models here.


class product(models.Model):
    name = models.CharField(max_length=50)#string
    color = models.CharField(max_length=50)#string
    price = models.DecimalField(max_digits=10,decimal_places=5)#cimal use when you wont ccalculation the price and accuracy number
    quintity = models.IntegerField()#int
    tax = models.FloatField()#float
    total = models.DecimalField(max_digits=10,decimal_places=5)
    date = models.DateTimeField(auto_now_add=True)#date and time
    net = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def __str__(self):
        return self.name