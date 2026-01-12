import logging
import os

# start logging
logger = logging.getLogger()
logging.getLogger().setLevel(logging.INFO)

# Get the env variable
raw_bucket = os.getenv('RAW_BUCKET')
standardized_bucket = os.getenv('STANDARDIZED_BUCKET')


def lambda_handler(event, context):
    logging.info (f"the name of the raw bucket is {raw_bucket}")
    logging.info(f"This is the name of the standardized bucket {standardized_bucket}")
    return "environmnet variable successfully retrieved"