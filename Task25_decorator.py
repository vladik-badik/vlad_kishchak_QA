def call_counter(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            with open(filename, 'w') as f:
                f.write(f"Function {func.__name__} was called {wrapper.count} times")
            return func(*args, **kwargs)
        wrapper.count = 0
        return wrapper
    return decorator
@call_counter('data.txt')
def add():
    print("hello world")

add()
add()