from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Feedback)
admin.site.register(FeedbackResponse)
admin.site.register(Card)
admin.site.register(Category)
admin.site.register(PaymentOrder)
admin.site.register(District)
admin.site.register(Image)
admin.site.register(City)
admin.site.register(Favorite)