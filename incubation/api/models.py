from django.db import models


class BookingForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    address =  models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    note = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name