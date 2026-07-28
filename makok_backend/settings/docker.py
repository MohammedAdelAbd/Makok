from .custom import IN_DOCKER
from .base import MIDDLEWARE

if IN_DOCKER:
    print("Running in Docker mode...")
    assert MIDDLEWARE[:1] == [
        'django.middleware.security.SecurityMiddleware',
    ]
