from django.shortcuts import render, redirect

# Create your views here.
def redirect_to_food(request):
    return render(request, 'home/redirect_to_food.html', context={})

    # return redirect(request, 'food:index')