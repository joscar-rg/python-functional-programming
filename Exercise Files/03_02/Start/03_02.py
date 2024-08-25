numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def double(x):
    return x * 2

doubled_list_functional = list(map(double, numbers_list))
print(doubled_list_functional)