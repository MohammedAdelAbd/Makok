import os

from .misc import yaml_coerce

def get_env_setting(prefix):
    """
    Get environment variables with the given prefix and return them as a dictionary.
    The values are coerced using yaml_coerce to allow for complex data types.
    """
    settings = {}
    for key, value in os.environ.items():
        if key.startswith(prefix):
            settings[key[len(prefix):]] = yaml_coerce(value)
    return settings
