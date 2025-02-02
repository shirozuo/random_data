import os
import sys

# Main entry point for the Django project
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "random_data.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
