import os.path
from split_settings.tools import include, optional
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Include settings from the 'components' directory
ENVVAR_SETTINGS_PREFIX = 'CORESETTINGS_'

LOCAL_SETTINGS_PATH = os.getenv(
    f'{ENVVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH'
)

if not LOCAL_SETTINGS_PATH:
    LOCAL_SETTINGS_PATH = 'local/settings.dev.py'


if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = os.path.join(BASE_DIR, LOCAL_SETTINGS_PATH)


include(
    'base.py',
    'custom.py',
    optional(LOCAL_SETTINGS_PATH),
    'envvars.py',
    'docker.py',
    'logging.py',
)
