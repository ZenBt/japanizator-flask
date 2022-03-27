import decouple
class Configuration:
    SECRET_KEY = decouple.config('SECRET_KEY')
    DEBUG = decouple.config('DEBUG')
    JSON_AS_ASCII = False
    