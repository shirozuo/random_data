import os
import django
import logging
from apscheduler.schedulers.blocking import BlockingScheduler

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'random_data.settings')
django.setup()

from generator.tasks import generate_random_number

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("scheduler")

# Create a scheduler
scheduler = BlockingScheduler()

# Define a scheduled task to generate a random number every 5 seconds
@scheduler.scheduled_job('interval', seconds=5)
def scheduled_task():
    logger.debug("Starting task to generate a random number")
    try:
        generate_random_number()
        logger.debug("Task completed successfully")
    except Exception as e:
        logger.error(f"Error during task execution: {e}")

# Start the scheduler
logger.debug("Starting the scheduler")
scheduler.start()
