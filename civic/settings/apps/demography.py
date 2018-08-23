import os

CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")
DEMOGRAPHY_AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
DEMOGRAPHY_AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
DEMOGRAPHY_AWS_REGION = "us-east-1"
DEMOGRAPHY_AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
DEMOGRAPHY_AWS_S3_UPLOAD_ROOT = "election-results/data/us-census"
DEMOGRAPHY_AWS_ACL = "public-read"
DEMOGRAPHY_AWS_CACHE_HEADER = "max-age=31536000"
