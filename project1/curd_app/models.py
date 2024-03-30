from django.db import models


class HotelBooking(models.Model):
    customer_first_name = models.CharField(max_length=20)
    customer_last_name = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=20)
    customer_email = models.EmailField()
    customer_phone_no = models.IntegerField()
    check_in = models.DateField(auto_now_add=True)
    check_out = models.DateField(auto_now=True)

