from django.contrib import admin
from .models import Restaurant, Table, Booking, MenuItem

admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Booking)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'phone')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'number', 'capacity')
    list_filter = ('restaurant',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'name', 'price', 'available')
    list_filter = ('restaurant', 'available')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time', 'guests', 'is_cancelled')
    list_filter = ('date', 'is_cancelled')
