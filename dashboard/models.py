from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CATEGORY=(
    ('Food','Food'),
    ('Electronics','Electronics'),
    ('Clothing','Clothing'),
)
class Product(models.Model):
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=20,choices=CATEGORY,default='Food')
    quantity=models.PositiveIntegerField()
    def __str__(self):
        return f'{self.name}'
class Order(models.Model):
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField()
    staff = models.ForeignKey(User,on_delete=models.CASCADE)   
    date=models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return f'product {self.product} ,amount {self.order_quantity} ,ordered_by {self.staff.username}'
class Profile(models.Model):
    staff = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    image=models.ImageField(default='rename.jpg',upload_to='profile_images') 

    def __str__(self):
        return f'{self.staff.username}-profile'       
