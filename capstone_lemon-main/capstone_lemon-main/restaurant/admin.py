from django.contrib import admin
from .models import Booking, Menu

# Custom admin configuration for the Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_of_guests', 'booking_date')
    search_fields = ('name',)
    list_filter = ('booking_date',)
    ordering = ('-booking_date',)  # Orders bookings by date, newest first

# Custom admin configuration for the Menu model
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory')
    search_fields = ('title',)
    list_filter = ('price',)
    ordering = ('title',)  # Orders menu items alphabetically by title
