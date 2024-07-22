import os
import logging
import random
from django.http import JsonResponse
from .models import RandomNumber
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'random_data.settings')
django.setup()

# Logger for tasks
logger = logging.getLogger("tasks")
logger.debug("Task launched")

# Function to generate a random number
def generate_random_number():
    number = random.randint(1, 100)
    try:
        # Create a record with the random number in the database
        random_number = RandomNumber.objects.create(number=number)
        logger.debug(f"Generated random number: {number}")
        return JsonResponse({'number': random_number.number})
    except Exception as e:
        # Log error if saving the number fails
        logger.error(f"Error saving the number: {e}")
