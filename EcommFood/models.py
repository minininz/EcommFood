from django.db import models
from django.conf import settings

# Create your models here.

class Products(models.Model):
    
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    typee=models.CharField(max_length=50)
    desc=models.TextField(default="per kg")
    offer=models.BooleanField(default=False)
    

class OrderPdts(models.Model):

    
    ordered = models.BooleanField(default=False)
    pdt = models.ForeignKey(Products,on_delete=models.CASCADE)
    qty=models.IntegerField(default='1')

    def gettotalpdtprice(self):
        return self.qty*self.pdt.price
    
   

class Order(models.Model):
   
    pdt = models.ManyToManyField(OrderPdts)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered=models.BooleanField(default=False)

    def getbilltotal(self):
        total=0
        order_qs=Order.objects.filter(ordered=False)
        if order_qs.exists():
            order=order_qs[0]
            for orderpdt in order.pdt.all():
                total = total + orderpdt.gettotalpdtprice()
        return total
     