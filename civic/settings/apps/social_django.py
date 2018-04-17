import os

AUTHENTICATION_BACKENDS = (
    'social_core.backends.slack.SlackOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
LOGIN_URL = '/login/slack/'
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_SLACK_KEY = os.getenv('SOCIAL_AUTH_SLACK_KEY')
SOCIAL_AUTH_SLACK_SECRET = os.getenv('SOCIAL_AUTH_SLACK_SECRET')
SOCIAL_AUTH_SLACK_TEAM = 'politicobn'
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False if DEBUG else True  # noqa: F821
