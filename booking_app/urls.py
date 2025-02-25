# booking_app/urls.py
from django.urls import path
from . import views


app_name = 'booking'

urlpatterns = [
    path('', views.home, name='home'),
    path('book-table/', views.book_table, name='book_table'),
    path('book/<int:restaurant_id>/', views.book_table, name='book_table'),
    path('bookings/', views.view_bookings, name='view_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('register/', views.register, name='register'),  # Add registration URL
    path('manage-menu/<int:restaurant_id>/',
         views.manage_menu, name='manage_menu'),
    path('edit-menu-item/<int:item_id>/',
         views.edit_menu_item, name='edit_menu_item'),
    path('delete-menu-item/<int:item_id>/',
         views.delete_menu_item, name='delete_menu_item'),
    path('calendar/', views.calendar_view,
         name='calendar_view'),  # New calendar view
    path('get-events/', views.get_events,
         name='get_events'),  # New JSON events URL
]
