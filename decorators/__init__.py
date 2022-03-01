def simpleDecorator(message: str = None):
    if message is not None and message != "":
        print(message)

    def wrapper(func):
        def inner(*args, **kwargs):
            return func(*args, **args)

        return inner

    return wrapper