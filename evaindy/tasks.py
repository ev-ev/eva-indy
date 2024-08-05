"""App Tasks"""

# Standard Library
import logging

# Third Party
from celery import shared_task

logger = logging.getLogger(__name__)

# Create your tasks here


# evaindy Task
@shared_task
def evaindy_task():
    """evaindy Task"""

    pass
