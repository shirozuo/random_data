import random

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from .models import RandomNumber


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'generator/index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'generator/login.html')


class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        return redirect('login')


class GenerateRandomNumberView(View):
    def get(self, request):
        number = random.randint(1, 100)
        random_number = RandomNumber.objects.create(number=number)
        return JsonResponse({'number': random_number.number})


class GetLatestNumberView(View):
    def get(self, request):
        latest_number = RandomNumber.objects.latest('timestamp')
        return JsonResponse({'number': latest_number.number})
