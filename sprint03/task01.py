def outer(name):
    nm = name
    def inner():
        print(f"Hello, {nm}!")
    return inner
