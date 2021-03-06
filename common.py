import os
from dotenv import load_dotenv
import logging
import datetime
from pathlib import Path

class Common():

    load_dotenv()
    logging_level = int(os.getenv('logging_level'))
    filename = datetime.datetime.now().strftime("%Y%m%d") + "_banano_node_bot.log"
    logdir = Path(__file__).resolve().parent / "logs" 
    # Make directory if it doesn't already exist
    if not os.path.exists(logdir):
        try:
            os.makedirs(logdir)
        except OSError as e:
            print(f"Error creating {logdir} :", e)
            exit()
    logfile = logdir / filename
    logging.basicConfig(filename=logfile, format='%(asctime)-10s - %(levelname)s - %(message)s', level=logging_level)
    logger = logging.getLogger(__name__)

    def __init__(self):
        pass

    # Helper function for changing seconds into nice formatted string of 
    # number of days, hours, minutes, and seconds
    @staticmethod
    def get_days_from_secs(secs):
        # Turn seconds into days, hours, minutes, seconds
        time = int(secs)
        # Break down into days, hours, minutes, seconds
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hours = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        return f"{day} days, {hours} hours, {minutes} minutes, and {seconds} seconds"

    # Helper function for generic logging
    @staticmethod
    def log(msg):
        Common.logger.info(msg)

    # Convert units raw to banano. Banano is divisible by 30.
    @staticmethod
    def rawToBanano(raw):
        return raw / 1e30

    @staticmethod
    def log_error(msg):
        Common.logger.error(msg)

    # Helper function for logging bot commands
    # <- {User} : {command}
    @staticmethod
    def logit(ctx):
        Common.logger.info(f"-> {ctx.message.author} : {ctx.command}")
        

