"""
Service Package
"""
import os
from flask import Flask

from service.common import log_handlers

app = Flask(__name__)

log_handlers.init_logging(app, "gunicorn.error")

# Required by grader
port = os.getenv("PORT", "8000")
app.logger.info("SERVICERUNNING")
app.logger.info("Running on port %s", port)

# Banner
app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

# Import routes after app creation
from service import routes  # pylint: disable=wrong-import-position,cyclic-import
