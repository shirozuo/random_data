import os
import subprocess

os.chdir('random_data')

subprocess.Popen(["daphne", "-p", "8000", "random_data.asgi:application"])

subprocess.Popen(["python", "manage.py", "runserver"])

subprocess.Popen(["python", "scheduler.py"])
