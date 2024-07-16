from django.shortcuts import render

# Create your views here.
def redirect_to_food(request):
    return render(request, 'home/redirect_to_food.html', context={})