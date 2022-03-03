class CvToolDecorator:
    @staticmethod
    def checkParam(paramName, paramTypeList: list = [], paramRange: list = []):
        def wrapper(func):
            def inner(*args, **kwargs):
                _arg = kwargs.get(paramName, None)
                if _arg is not None:
                    if len(paramTypeList) > 0:
                        assert type(
                            _arg
                        ) in paramTypeList, "input error, should be a {}".format(
                            " or ".join(list(str(x) for x in paramTypeList)))

                    if len(paramRange) > 0:
                        assert _arg in paramTypeList, "input error"

                return func(*args, **kwargs)

            return inner

        return wrapper

    @staticmethod
    def simpleDecorator(message: str = None):
        if message is not None and message != "":
            print(message)

        def wrapper(func):
            def inner(*args, **kwargs):
                return func(*args, **kwargs)

            return inner

        return wrapper
