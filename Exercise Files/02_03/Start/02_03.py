def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def combine_2_and_3(func):
    return func(2, 3)

print(combine_2_and_3(max))

def combine_names(func):
    return  func('Jose', 'Rodriguez')

def append_with_space(str1, str2):
    return f'{str1} {str2}'

def get_gouvernment_form_notetion(first, last):
    return f'{last.upper()}, {first.upper()}'

print(combine_names(get_gouvernment_form_notetion))