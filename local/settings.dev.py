import colorlog

SECRET_KEY = "django-insecure-h23ty&5-npm6zu%nuwzob-@q)n$-k8=*!k+#-lq13&)suj=o+c"
DEBUG = True

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter('%(log_color)s%(levelname)s:%(name)s:%(message)s'))
logger = colorlog.getLogger('example')
logger.addHandler(handler)
