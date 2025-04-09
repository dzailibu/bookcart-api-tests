"""Sets up and configures the global logger for the test framework."""
import logging

# Log to the current directory (explicitly)
log_file = "test_run.log"

# Create logger
logger = logging.getLogger("BookCartLogger")
logger.setLevel(logging.INFO) # SET LOG LEVEL HERE (DEBUG,INFO,WARNING,ERROR,CRITICAL)

# Create file handler
file_handler = logging.FileHandler(log_file)

# Create formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)

# Add handler and log test start
logger.addHandler(file_handler)
logger.info("\nNEW TEST STARTED")
