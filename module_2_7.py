def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(3)
print_params(b = 4)
print_params(4, 2, 6)
print_params(25)
print_params(c = [1, 2, 3])

values_list = [3, 'dfsdgf', True]
values_dict = {'a': 5462456, 'b': 'sssdfgsdf', 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list2 = [54.32, 'Строка']
print_params(*values_list2, 42)
