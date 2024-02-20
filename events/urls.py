from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('register/<int:event_id>/', views.register_event, name='register_event'),
    path('add/', views.add_event, name='add_event'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('create_category/', views.create_category, name='create_category'),
    path('category-description/<int:category_id>/', views.category_description, name='category_description'),
]
