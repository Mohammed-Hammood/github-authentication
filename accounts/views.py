from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import RandomNumberModel


@login_required
def home_view(request):
    today = timezone.datetime.today()
    query = RandomNumberModel.objects.filter(timestamp=today).last()
    if not query:
        query = RandomNumberModel.objects.create(user = request.user)
    query.update_random_number()
    context = {
        "query": query, 
        "last_updated_in_seconds": query.last_updated_in_seconds()
        }
    if request.method == 'POST':
        return JsonResponse({
            "random_number":query.random_number, 
            "last_updated_in_seconds":query.last_updated_in_seconds()
            })
    return render(request, 'home.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts_app:home")
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect("accounts_app:login")


@login_required
def profile_view(request):
    return render(request, 'profile.html', {})
