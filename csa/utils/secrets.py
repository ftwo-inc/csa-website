def get_secret(key='', default=''):
    from decouple import config
    return config(key)