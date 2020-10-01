#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
"""
import os         # we import os 
import sys        # we import sys 


def main():
    """
    Command-line entry-point to manage Django app.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_hello_world.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as e:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from e
        
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
