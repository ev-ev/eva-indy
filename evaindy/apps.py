"""App Configuration"""

# Django
from django.apps import AppConfig

# AA evaindy App
from evaindy import __version__


class EvaindyConfig(AppConfig):
    """App Config"""

    name = "evaindy"
    label = "evaindy"
    verbose_name = f"evaindy App v{__version__}"
