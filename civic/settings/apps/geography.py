import os

CENSUS_API_KEY = os.getenv('CENSUS_API_KEY')
GEOGRAPHY_AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
GEOGRAPHY_AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
GEOGRAPHY_AWS_REGION = 'us-east-1'
GEOGRAPHY_AWS_S3_BUCKET = os.getenv('AWS_S3_BUCKET')
GEOGRAPHY_AWS_S3_UPLOAD_ROOT = 'election-results/cdn'
GEOGRAPHY_AWS_ACL = 'public-read'
GEOGRAPHY_AWS_CACHE_HEADER = 'max-age=3600'
