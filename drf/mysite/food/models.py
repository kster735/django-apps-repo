from django.db import models
from datetime import datetime
# from django.db.models.functions import Now
from django.utils import timezone, timesince

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.FloatField()
    item_image = models.ImageField(upload_to='Images/', default='Images/None/Noimg.jpeg')
    item_created_at = models.DateTimeField(auto_created=True)
    item_last_updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.item_name

    def updated_before(self):
        return timesince.timesince(self.item_last_updated_at)