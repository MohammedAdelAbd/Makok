from core.utils.collections import deep_update
from core.utils.settings import get_env_setting


deep_update(globals(), get_env_setting(ENVVAR_SETTINGS_PREFIX))  #type: ignore
