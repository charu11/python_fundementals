from functools import wraps


def add_wrapping(item):
    @wraps(item)
    def wrapped_item():
        return 'a wrapped up box of {}'.format(str(item()))
    return wrapped_item


@add_wrapping
def new_gpu():
    return 'a new tesla gpu'


print(new_gpu())


@add_wrapping
def bicycle():
    return 'got a new bicycle'


print(bicycle())

print(new_gpu.__name__)

