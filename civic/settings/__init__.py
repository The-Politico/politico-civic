"""Django settings for datalab project."""

from split_settings.tools import include

include(
    'components/base.py',
    'components/apps.py',
    'components/databases.py',
    'components/middleware.py',
    'components/templates.py',
    'components/logging.py',
    'components/statics.py',
    'components/internationalization.py',
    'components/passwords.py',
    'apps/*.py'
)
