def tol(length, fill):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, list):
                result = list(result)
            if len(result) < length:
                result.extend([fill] * (length - len(result)))
            elif len(result) > length:
                result = result[:length]
            return result
        return wrapper
    return decorator

@tol(5, 0)
def get_numbers():
    return [1, 2, 3]

@tol(5, 0)
def get_more_numbers():
    return [1, 2, 3, 4, 5, 6, 7]

@tol(5, 0)
def get_string():
    return "abc"

print(get_numbers())         # Output: [1, 2, 3, 0, 0]
print(get_more_numbers())    # Output: [1, 2, 3, 4, 5]
print(get_string())          # Output: ['a', 'b', 'c', 0, 0]
