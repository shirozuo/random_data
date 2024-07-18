from django.urls import path
from .views import GenerateRandomNumberView, GetLatestNumberView

urlpatterns = [
    path('generate/', GenerateRandomNumberView.as_view(), name='generate_random_number'),
    path('latest/', GetLatestNumberView.as_view(), name='get_latest_number'),
]
