import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Load .env file from the project root
project_root = Path(__file__).resolve().parent.parent
try:
    import dotenv
    dotenv.load_dotenv(project_root / '.env')
except ImportError:
    pass # In production, env vars are usually set by the system

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
application = get_wsgi_application()
