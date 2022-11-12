from django.db import models
from accounts.models import Account
from category.models import Product

# Create your models here.

#Cart Table
class Cart(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    
    
    def get_product_price(self):
        price=[self.product.price]
        return sum(price)


class Whishlist(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)        