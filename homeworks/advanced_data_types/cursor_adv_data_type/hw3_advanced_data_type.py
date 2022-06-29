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
