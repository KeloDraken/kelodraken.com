from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

APPS = [
    "home",
]

ROOT_URLCONF = "mysite.config.urls"

WSGI_APPLICATION = "mysite.config.wsgi.application"        
