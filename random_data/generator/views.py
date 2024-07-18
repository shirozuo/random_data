from django.http import JsonResponse
from django.views import View
from .models import RandomNumber
import random


class GenerateRandomNumberView(View):
    def get(self, request):
        number = random.randint(1, 100)
        random_number = RandomNumber.objects.create(number=number)
        return JsonResponse({'number': random_number.number})


class GetLatestNumberView(View):
    def get(self, request):
        latest_number = RandomNumber.objects.latest('timestamp')
        return JsonResponse({'number': latest_number.number})
