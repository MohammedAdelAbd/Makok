try:
    import yaml
except ImportError:
    yaml = None
    import json as _json


def yaml_coerce(value):
    if isinstance(value, str):
        if yaml is not None:
            try:
                return yaml.safe_load(value)
            except yaml.YAMLError:
                return value
        try:
            return _json.loads(value)
        except ValueError:
            return value
