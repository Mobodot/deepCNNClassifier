import os
import sys
import logging


# '[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s'

LOG_STR = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
LOG_DIR = "logs"
LOG_FILE = "running_logs.log"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)


logging.basicConfig(
                    level=logging.INFO,
                    format=LOG_STR,
                    handlers=[
                        logging.FileHandler(LOG_FILE_PATH),
                        logging.StreamHandler(sys.stdout)
                    ])


logger = logging.getLogger("deepClassifier")
