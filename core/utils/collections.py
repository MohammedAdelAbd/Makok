def deep_update(target: dict, source: dict) -> dict:
    """
    Recursively updates the target dictionary with the source dictionary.
    If a key exists in both dictionaries and the corresponding values are also dictionaries,
    the function will recursively update those nested dictionaries instead of overwriting them.

    :param target: The dictionary to be updated.
    :param source: The dictionary containing updates to be applied to the target.
    :return: The updated target dictionary.
    """
    for key, value in source.items():
        if isinstance(value, dict) and key in target and isinstance(target[key], dict):
            deep_update(target[key], value)
        else:
            target[key] = value
    return target
