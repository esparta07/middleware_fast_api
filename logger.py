import logging
import sys
from logtail import LogtailHandler

token = 'yxMAFf3cq54awjjpYtehpcRJ'

# Get logger
logger = logging.getLogger()

# Create formatter
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

# Create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("app.log")
better_stack_handler = LogtailHandler(source_token=token)

# Set formatter
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
better_stack_handler.setFormatter(formatter)

# Add handler to the logger
logger.handlers = [stream_handler, file_handler, better_stack_handler]

# Set log level
logger.setLevel(logging.INFO)
