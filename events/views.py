from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from .forms import EventForm, RegistrationForm, CategoryForm
from .models import Category, Event, Registration
from django.contrib import messages

def category_description(request, category_id):
    category = Category.objects.get(id=category_id)
    return JsonResponse({'description': category.description})

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events:calendar')
    else:
        form = CategoryForm()
    return render(request, 'events/create_category.html', {'form': form})
def calendar_view(request):
    events = Event.objects.all()
    events_json = serializers.serialize('json', events)
    return render(request, 'events/calendar.html', {'events_json': events_json})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Мероприятие успешно добавлено.')
            return redirect('events:calendar')
        else:
            messages.error(request, 'Ошибка при добавлении мероприятия.')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})

def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form._bound_fields_cache['first_name'].data
            last_name = form._bound_fields_cache['last_name'].data
            middle_name = form._bound_fields_cache['middle_name'].data
            email = form._bound_fields_cache['email'].data
            birth_date = form._bound_fields_cache['birth_date'].data
            phone_number = form._bound_fields_cache['phone_number'].data
            registration = Registration(first_name=first_name, last_name=last_name, middle_name=middle_name,
                                        email=email, birth_date=birth_date, phone_number=phone_number, event_id=event_id)
            registration.save()
            messages.success(request,
                             'Вы успешно зарегистрировались на мероприятие. Вы будете перенаправлены на календарь через 6 секунд.')
            return redirect('events:calendar')
    else:
        form = RegistrationForm(request.GET)
    return render(request, 'events/register_event.html', {'form': form, 'event': event})
