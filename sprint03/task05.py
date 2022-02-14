def logger(func):
    def inner(*args, **kwargs):
        args_l = [i for i in args] + [i for i in kwargs.values()]
        res = f"Executing of function {func.__name__} with arguments " + ", ".join(str(i) if type(i) != str else i for i in args_l) + '...'
        if not func.__name__ == "print_arg":
            print(res)
            return func(*args_l)
        else:
            func(*args_l)
            print(res)
    return inner

@logger
def concat(*args, **kwargs):
    return "".join(str(i) for i in ([i for i in args] + [i for i in kwargs.values()]))
