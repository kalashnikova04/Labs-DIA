from django.shortcuts import get_object_or_404, render

from .models import Food
from .models import Choice

def index(request):
    food_list = Food.objects.all()
    context = {'food_list':food_list}
    return render(request, 'polls/index.html', context)


def details(request, food_id):
    food_list = Food.objects.all()
    for i in food_list:
        if i.id == food_id:
            food = i
    description = get_object_or_404(Choice, pk=food_id)
    return render(request, 'polls/details.html', {'food': food, 'description': description})