from django.db import models

# Model representing a restaurant booking
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.name
    
# Model representing a menu item
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title}: ${self.price}'
