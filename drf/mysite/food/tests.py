from django.test import TestCase
from .models import Item
from django.utils import timesince, timezone
from datetime import datetime
from zoneinfo import ZoneInfo
# Create your tests here.
class ItemModelTests(TestCase):

    def test_updated_before(self):
        """
        Should return the time ellapsed since last time the item was updated.  
        """

        # tzname = self.request.session.get("django_timezone")

        value = timezone.datetime(year=2024, month=7, day=16, hour=10, minute=40, second=23, tzinfo=ZoneInfo('UTC'))
        oldItem = Item(item_created_at= value, item_last_updated_at= value)
        
        want = timesince.timesince(oldItem.item_last_updated_at)
        got = oldItem.updated_before()

        self.assertEqual(got, want)