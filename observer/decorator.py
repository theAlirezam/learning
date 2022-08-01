def notify_observer(message=''):

    def decorated_method(func):

        def wrapped(obj, *args, **kwargs):
            result = func(obj, *args, **kwargs)
            for observer in obj.observer:
                observer.send(message)
            return result

        return wrapped

    return decorated_method
