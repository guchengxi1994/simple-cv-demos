class CvToolDecorator:
    @staticmethod
    def checkParam(paramName:str = "",
                   paramIndex: int = -1,
                   paramTypeList: list = [],
                   paramRange: list = []):
        """using parameter's name is recommended

           Params
           -------
           paramName : the parameter name in **kwargs
           paramIndex : optional, the parameter index in *args
           paramTypeList : parameter types ,such as [int,str,tuple,...]
           paramRange : parameter values ,such as ["I","love","China"]

        """
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
                        assert _arg in paramRange, "input error"

                if paramIndex != -1 and paramIndex < len(args):
                    _arg = args[paramIndex]
                    if len(paramTypeList) > 0:
                        assert type(
                            _arg
                        ) in paramTypeList, "input error, should be a {}".format(
                            " or ".join(list(str(x) for x in paramTypeList)))

                    if len(paramRange) > 0:
                        assert _arg in paramRange, "input error"

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
