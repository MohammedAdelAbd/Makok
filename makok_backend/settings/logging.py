LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'filters': [],
        },
    },
    'formatters': {
        'standard': {
            'format': '{asctime} {levelname} {name} {message}',
            'style': '{',
        },
        'verbose': {
            'format': '[{asctime}] {levelname} {name} {message}',
            'style': '{',
        },
    },
    'loggers': {
       logger_name: {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        } for logger_name in ['django', 'myapp', 'another_module', 'core', 'utils', 'api', 'services', 'tasks', 'views', 'models']
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
