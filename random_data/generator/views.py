import random
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import RandomNumber


# View for the index page
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'generator/index.html')


# View for the login page
class LoginView(View):
    def get(self, request):
        return render(request, 'generator/login.html')


# View for logging out
class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        return redirect('login')


# View for generating a random number
class GenerateRandomNumberView(View):
    def get(self, request):
        number = random.randint(1, 100)
        random_number = RandomNumber.objects.create(number=number)
        return JsonResponse({'number': random_number.number})


# View for getting the latest generated number
class GetLatestNumberView(View):
    def get(self, request):
        latest_number = RandomNumber.objects.latest('timestamp')
        return JsonResponse({'number': latest_number.number})


# View for getting all generated numbers
class GetAllNumbersView(View):
    def get(self, request):
        all_numbers = RandomNumber.objects.all().values('number', 'timestamp')
        response_data = list(all_numbers)
        return JsonResponse({'numbers': response_data})
