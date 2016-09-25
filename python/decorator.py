from datetime import datetime

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s %s():' % ('begin ', text, func.__name__))
            func(*args, **kw)
            print('%s %s %s():' % ('end ', text, func.__name__))
        return wrapper
    return decorator


@log('run')
def now():
    print datetime.now().date()


now()

