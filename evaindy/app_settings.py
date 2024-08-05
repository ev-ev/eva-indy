"""App Settings"""

# Django
from django.conf import settings

# put your app settings here


EVAINDY_SETTING_ONE = getattr(settings, "EVAINDY_SETTING_ONE", None)
