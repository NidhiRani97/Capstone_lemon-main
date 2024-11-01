#!/usr/bin/env python
"""Django command-line utility for performing administrative tasks."""
import os
import sys


def main():
    """Execute Django administrative commands."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "littlelemon.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as error:
        raise ImportError(
            "Couldn't import Django. Ensure it is installed and "
            "present in your PYTHONPATH environment variable. Did you "
            "activate the virtual environment?"
        ) from error
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
