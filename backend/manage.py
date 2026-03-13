#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

def main():
    """Run administrative tasks."""
    # Add the project root (D:/ShSchool02) to sys.path
    current_path = Path(__file__).resolve().parent
    project_root = current_path.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    # Load .env file from the project root
    try:
        import dotenv
        dotenv.load_dotenv(project_root / '.env')
    except ImportError:
        print("Warning: 'python-dotenv' not installed. Falling back to system environment variables.")

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
