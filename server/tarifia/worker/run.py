from tarifia import tasks
from tarifia.logfire import configure_logfire
from tarifia.logging import configure as configure_logging
from tarifia.posthog import configure_posthog
from tarifia.sentry import configure_sentry
from tarifia.worker import broker

configure_sentry()
configure_logfire("worker")
configure_logging(logfire=True)
configure_posthog()

__all__ = ["broker", "tasks"]
