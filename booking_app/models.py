# booking_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Restaurant(models.Model):
    """
    Represents a restaurant in the system.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Table(models.Model):
    """
    Represents a table in a restaurant.
    """
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='tables')
    number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number} at {self.restaurant.name}"


class MenuItem(models.Model):
    """
    Represents a menu item available at a restaurant.
    """
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)


class Booking(models.Model):
    """
    Represents a booking for a table in a restaurant.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.number_of_guests} at {self.booking_time} on {self.booking_date}"

    def clean(self):
        # Prevent double bookings
        if self.table and self.booking_date and self.booking_time:
            conflicting_bookings = Booking.objects.filter(
                table=self.table,
                booking_date=self.booking_date,
                booking_time=self.booking_time
            ).exclude(pk=self.pk)  # Exclude the current booking if updating

            if conflicting_bookings.exists():
                raise ValidationError(
                    "This table is already booked for this date and time.")
        super().clean()  # Call the parent's clean() method

    def save(self, *args, **kwargs):
        self.clean()  # Run validation
        super().save(*args, **kwargs)
