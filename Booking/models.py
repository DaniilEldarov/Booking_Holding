from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='media/avatars')
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    new_field = models.CharField(max_length=255, blank=True, null=True)  # Adjust name

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    expire_date = models.DateField()

class Category(models.Model):
    title = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        ancestors = []
        category = self
        while category:
            ancestors.append(category.title)
            category = category.parent_category
        return ' > '.join(reversed(ancestors))

class City(models.Model):
    title = models.CharField(max_length=100)

class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    geo = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    promo_video = models.FileField(blank=True, null=True,upload_to='media/videos')
    is_active = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='media/images')

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='media/images')
    is_main = models.BooleanField(default=False)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class FeedbackResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PaymentOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
