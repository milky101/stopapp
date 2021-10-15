from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product', default='pix.jpg')

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='product', default='pix.jpg')
    description =models.TextField()
    featured = models.BooleanField()
    latest = models.BooleanField()
    avaliable = models.BooleanField()
    min = models.IntegerField(default=1)
    max = models.IntegerField(default=100)


    def __str__(self):
        return self.name


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket_no = models.CharField(max_length=36)
    quantity = models.IntegerField()
    paid_order = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



class Slide(models.Model):
    image = models.ImageField(upload_to='slidepix', default='slide.jpeg')
    title = models.CharField(max_length=30)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    basket_no = models.CharField(max_length=36)
    pay_code = models.CharField(max_length=36)
    paid_order = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
       