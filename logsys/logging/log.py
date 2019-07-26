
import logging
from pprint import pformat
from flask import request

from flask_logconfig import request_context_from_record


class RequestFilter(logging.Filter):
    """Impart contextual information related to Flask HTTP request."""

    def filter(self, record):
        """Attach request contextual information to log record."""

        with request_context_from_record(record):
            # logging.debug("RequestFilter.......")
            record.environ_info = request.environ.copy()
            record.environ_text = pformat(record.environ_info)
        return True
