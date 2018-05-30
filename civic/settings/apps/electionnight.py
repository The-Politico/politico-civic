import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ELECTIONNIGHT_AWS_S3_BUCKET = os.getenv('ELECTIONNIGHT_AWS_S3_BUCKET')
ELECTIONNIGHT_RESULTS_STATIC_DIR = 'static_results'
ELECTIONNIGHT_AWS_S3_STATIC_ROOT = os.getenv(
    'ELECTIONNIGHT_AWS_S3_STATIC_ROOT'
)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, ELECTIONNIGHT_RESULTS_STATIC_DIR)
]
ELECTIONNIGHT_RESULTS_DAEMON_INTERVAL = 12
CIVIC_TWITTER_CONSUMER_KEY = os.getenv('CIVIC_TWITTER_CONSUMER_KEY')
CIVIC_TWITTER_CONSUMER_SECRET = os.getenv('CIVIC_TWITTER_CONSUMER_SECRET')
CIVIC_TWITTER_ACCESS_TOKEN_KEY = os.getenv('CIVIC_TWITTER_ACCESS_TOKEN_KEY')
CIVIC_TWITTER_ACCESS_TOKEN_SECRET = os.getenv(
    'CIVIC_TWITTER_ACCESS_TOKEN_SECRET'
)
