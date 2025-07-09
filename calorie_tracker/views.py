from django.shortcuts import render,redirect

# Create your views here.
from .models import FoodItem
from django.utils import timezone

def home(request):
    today = timezone.now().date()
    food_items = FoodItem.objects.filter(date_added=today)
    total_calories = sum(item.calories for item in food_items)
    return render(request, 'calorie_tracker/home.html', {
        'food_items': food_items,
        'total_calories': total_calories
    })

def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        print(f"Adding food: {name}-{calories}")
        if name and calories:
            FoodItem.objects.create(name=name, calories=calories)
    return redirect('home')

def delete_food(request, id):
    FoodItem.objects.filter(id=id).delete()
    return redirect('home')

def reset_day(request):
    today = timezone.now().date()
    FoodItem.objects.filter(date_added=today).delete()
    return redirect('home')