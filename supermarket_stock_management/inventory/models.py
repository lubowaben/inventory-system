from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    expiry_date = models.DateField()

    def __str__(self):
        return self.name

class StockTransaction(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('sale', 'Sale'),
        ('restock', 'Restock'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.pk is None:  # Check if the transaction is being created, not updated
            if self.transaction_type == 'sale':
                self.product.quantity -= self.quantity
            elif self.transaction_type == 'restock':
                self.product.quantity += self.quantity

            self.product.save()  # Save the updated product quantity

        super().save(*args, **kwargs)  # Call the original save method

class Profile(models.Model):
    USER_ROLES = (
        ('manager', 'Manager'),
        ('cashier', 'Cashier'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='cashier')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.message[:50]  





class Cashier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=10, unique=True,)  # Keep as a unique identifier
    contact_info = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name


