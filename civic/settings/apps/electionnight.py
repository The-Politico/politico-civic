import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ELECTIONNIGHT_AWS_S3_BUCKET = os.getenv('ELECTIONNIGHT_AWS_S3_BUCKET')
ELECTIONNIGHT_RESULTS_STATIC_DIR = 'static_results'
ELECTIONNIGHT_AWS_S3_STATIC_ROOT = "https://s3.amazonaws.com/staging.interactives.politico.com"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, ELECTIONNIGHT_RESULTS_STATIC_DIR)
]
