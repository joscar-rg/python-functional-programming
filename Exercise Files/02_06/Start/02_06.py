# HIGHER-ORDER FUNCTION, functions that either take other functions as parameters or return functions
def divide(x, y):
    return x / y

def second_argument_isnt_zero(func):
    def safe_version(*args):
        if args[1] == 0:
            print('Warning: someone is trying to divide by zero')
            return
        return func(*args)
    
    return safe_version

divide_safe = second_argument_isnt_zero(divide)

divide_safe(10, 0)
print(divide_safe(10, 2))