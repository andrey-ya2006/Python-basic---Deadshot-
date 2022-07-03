int_a = 55
print(id(int_a))
print('This is id of int_a ' + str(id(int_a)))
str_b = 'cursor'
print('This is id of str_b ' + str(id(str_b)))
set_c = {1, 2, 3}
print('This is id of set_c ' + str(id(set_c)))
lst_d = [1, 2, 3]
print('This is id of lst_d ' + str(id(lst_d)))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print('This is id of dict_e ' + str(id(dict_e)))
lst_d_new_element = [4, 5]
lst_d.append(lst_d_new_element)
print(lst_d)
print('This is id lst_d with new element ' + str(id(lst_d)))
lst_d.pop()
for var in lst_d_new_element:
    lst_d.append(var)
    print(id(lst_d))
    print(lst_d)
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))
print('Check int_a type ' + str(isinstance(int_a, int)))
print('Check str_b type ' + str(isinstance(str_b, str)))
print('Check set_c type ' + str(isinstance(set_c, set)))
print('Check lst_d type ' + str(isinstance(lst_d, list)))
print('Check dict_e type ' + str(isinstance(dict_e, dict)))
apples = 5
peaches = 7
print('Anna has {} apples and {} peaches.'.format(apples, peaches))
print('Anna has {0} apples and {1} peaches.'.format(apples, peaches))
print('Anna has {appl} apples and {peach} peaches.'.format(appl=apples, peach=peaches))
print('Anna has {appl:5} apples and {peach:3} peaches.'.format(appl=apples, peach=peaches))
print(f'Anna has {apples} apples and {peaches} peaches.')
print('Anna has %d apples and %d peaches.' % (apples, peaches))
dict_fruit = {'fruit1': 5, 'fruit2' : 7}
print('Anna has {fruit1} apples and {fruit2} peaches.'.format(**dict_fruit))
print(f'Anna has {dict_fruit["fruit1"]} apples and {dict_fruit["fruit2"]} peaches.')
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
lst_to_lst_comp = [ num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_to_lst_comp)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)
list_comprehension_to_regular = []
for x in range(10):
    if x % 2 == 0:
        list_comprehension_to_regular.append(x // 2)
    else:
        list_comprehension_to_regular.append(x * 10)
print(list_comprehension_to_regular)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

dict_compr = {x : x ** 2 for x in range(1, 11) if x % 2 == 1 }
print(dict_compr)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
dict_compr = {x : (x **2 if x % 2 == 1 else x // 0.5) for x in range(1, 11)}
print(dict_compr)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)
dict_compr_regular = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_compr_regular[x] = x ** 3
print(dict_compr_regular)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)
dict_compr_regular = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_compr_regular[x] = x ** 3
    else:
        dict_compr_regular[x] = x
print(dict_compr_regular)