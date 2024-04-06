from taskiq_redis import ListQueueBroker

from .settings import settings

broker = ListQueueBroker(settings.REDIS_URI.unicode_string())
