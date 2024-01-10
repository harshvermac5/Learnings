def my_decorator(func):
    def wrapper():
        print(f'running {func.__name__}')
        func()
        print(f'exiting {func.__name__}')
    return wrapper

@my_decorator
def do_this():
    print("Doing this!")

@my_decorator
def do_that():
    print("Doing that!")

do_this()
do_that()