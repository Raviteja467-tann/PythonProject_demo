import logging
import os

class logger_generator:
    @staticmethod
    def get_logger(name="automation"):
        logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
        os.makedirs(logs_dir, exist_ok=True)
        log_file = os.path.join(logs_dir, "MyLogs.log")
        print("Log path:", log_file)
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
            # Avoid adding duplicate handlers
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        return logger