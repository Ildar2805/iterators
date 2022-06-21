import datetime


def logger1(old_function):

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('info1.log', 'a') as file:
            file.write(f'Function "{old_function.__name__}" was called at {datetime.datetime.now()} with {args}. '
                       f'{result} was returned.\n')
        return result
    return new_function


def logger2(path):

    def log(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a') as file:
                file.write(f'Function "{old_function.__name__}" was called at {datetime.datetime.now()} with {args}. '
                           f'{result} was returned.\n')
            return result
        return new_function
    return log