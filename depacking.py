def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(2, 5, 6)
print_params(383883)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [23, 'kitty', False]
values_dict = {'a': 'blabla', 'b': True, 'c': 26262.6}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = True, 'i love my boyfriend'
print_params(*values_list_2, 42)