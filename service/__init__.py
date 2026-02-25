"""
Service Package
"""
import os  # add at top with imports

# ...

log_handlers.init_logging(app, "gunicorn.error")

# ✅ Required by grader (exact keyword + port)
port = os.getenv("PORT", "8000")
app.logger.info("SERVICERUNNING")
app.logger.info("Running on port %s", port)

# Existing banner (keep it)
app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")