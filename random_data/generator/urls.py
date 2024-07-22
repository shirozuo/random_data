from django.urls import path
from .views import *

# URL patterns for the application
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('generate/', GenerateRandomNumberView.as_view(), name='generate_random_number'),
    path('latest/', GetLatestNumberView.as_view(), name='get_latest_number'),
    path('all/', GetAllNumbersView.as_view(), name='get_all_numbers'),
]
