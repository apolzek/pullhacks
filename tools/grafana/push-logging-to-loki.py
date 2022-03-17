import logging
import logging_loki

logging_loki.emitter.LokiEmitter.level_tag = "level"

handler = logging_loki.LokiHandler(
    url="http://loki:3100/loki/api/v1/push",
    version="1",
)

logger = logging.getLogger("my-logger")
logger.setLevel(logging.DEBUG)

logging.addLevelName(15, "TRACE")


def trace(self, message, *args, **kws):
    if self.isEnabledFor(15):
        # Yes, logger takes its '*args' as 'args'.
        self._log(15, message, args, **kws)

logging.Logger.trace = trace


logger.addHandler(handler)

logger.critical(
    "Here's Something that's you need to address",
    extra={"tags": {"service": "my-service"}},
)

logger.error(
    "Something bad happened",
    extra={"tags": {"service": "my-service"}},
)

logger.warning(
    "Something bad happened but we can keep going",
    extra={"tags": {"service": "my-service"}},
)

logger.info(
    "Here's Something to read",
    extra={"tags": {"service": "my-service"}},
)

logger.debug(
    "Something on purpose",
    extra={"tags": {"service": "my-service"}},
)

logger.trace(
    "Something to follow",
    extra={"tags": {"service": "my-service"}},
)
