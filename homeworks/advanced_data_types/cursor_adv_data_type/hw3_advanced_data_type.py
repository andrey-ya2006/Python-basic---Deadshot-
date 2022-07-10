#1. Define the id of next variables:
int_a = 55
print('This is id of int_a ' + str(id(int_a)))
str_b = 'cursor'
print('This is id of str_b ' + str(id(str_b)))
set_c = {1, 2, 3}
print('This is id of set_c ' + str(id(set_c)))
lst_d = [1, 2, 3]
print('This is id of lst_d ' + str(id(lst_d)))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print('This is id of dict_e ' + str(id(dict_e)))

#2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d_new_element = [4, 5]
lst_d.append(lst_d_new_element)
print(lst_d)
print('This is id lst_d with new element ' + str(id(lst_d)))

#2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.pop()
for var in lst_d_new_element:
	lst_d.append(var)
	print(id(lst_d))
	print(lst_d)

#3. Define the type of each object from step 1.
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

#4*. Check the type of the objects by using isinstance.
print('Check int_a type ' + str(isinstance(int_a, int)))
print('Check str_b type ' + str(isinstance(str_b, str)))
print('Check set_c type ' + str(isinstance(set_c, set)))
print('Check lst_d type ' + str(isinstance(lst_d, list)))
print('Check dict_e type ' + str(isinstance(dict_e, dict)))

apples = 5
peaches = 7

#5. With .format and curly braces {}
print('Anna has {} apples and {} peaches.'.format(apples, peaches))

#6. By passing index numbers into the curly braces.
print('Anna has {0} apples and {1} peaches.'.format(apples, peaches))

#7. By using keyword arguments into the curly braces.
print('Anna has {appl} apples and {peach} peaches.'.format(appl=apples, peach=peaches))

#8*. With indicators of field size (5 chars for the first and 3 for the second)
print('Anna has {appl:5} apples and {peach:3} peaches.'.format(appl=apples, peach=peaches))

#9. With f-strings and variables
print(f'Anna has {apples} apples and {peaches} peaches.')

#10. With % operator
print('Anna has %d apples and %d peaches.' % (apples, peaches))

#11*. With variable substitutions by name (hint: by using dict)
dict_fruit = {'fruit1': 5, 'fruit2': 7}
print('Anna has {fruit1} apples and {fruit2} peaches.'.format(**dict_fruit))
print(f'Anna has {dict_fruit["fruit1"]} apples and {dict_fruit["fruit2"]} peaches.')

#12. Convert (1) to list comprehension
lst = []
for num in range(10):
	if num % 2 == 1:
		lst.append(num ** 2)
	else:
		lst.append(num ** 4)
print(lst)

lst_to_lst_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_to_lst_comp)

#13. Convert (2) to regular for with if-else
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)
list_comprehension_to_regular = []
for x in range(10):
	if x % 2 == 0:
		list_comprehension_to_regular.append(x // 2)
	else:
		list_comprehension_to_regular.append(x * 10)
print(list_comprehension_to_regular)

#14. Convert (3) to dict comprehension.
d = {}
for num in range(1, 11):
	if num % 2 == 1:
		d[num] = num ** 2
print(d)

dict_compr = {x: x ** 2 for x in range(1, 11) if x % 2 == 1}
print(dict_compr)

#15*. Convert (4) to dict comprehension.
d = {}
for num in range(1, 11):
	if num % 2 == 1:
		d[num] = num ** 2
	else:
		d[num] = num // 0.5
print(d)
dict_compr = {x: (x ** 2 if x % 2 == 1 else x // 0.5) for x in range(1, 11)}
print(dict_compr)

#16. Convert (5) to regular for with if.
dict_comprehension = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print(dict_comprehension)
dict_compr_regular = {}
for x in range(10):
	if x ** 3 % 4 == 0:
		dict_compr_regular[x] = x ** 3
print(dict_compr_regular)

#17*. Convert (6) to regular for with if-else.
dict_comprehension = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)
dict_compr_regular = {}
for x in range(10):
	if x ** 3 % 4 == 0:
		dict_compr_regular[x] = x ** 3
	else:
		dict_compr_regular[x] = x
print(dict_compr_regular)

#18. Convert (7) to lambda function
def foo(x, y):
	if x < y:
		return x
	else:
		return y


print(foo(5, 6))
my_lam = lambda x, y: x if x < y else y
print(my_lam(5, 6))

#19*. Convert (8) to regular function
foo = lambda x, y, z: z if y < x and x > z else y
print(foo(4, 7, 12))


def lambda_to_foo(x, y, z):
	if y < x and x > z:
		return z
	else:
		return y


print(lambda_to_foo(4, 7, 12))


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

#20. Sort lst_to_sort from min to max
print(sorted(lst_to_sort))

#21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))

#22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x * 2, lst_to_sort)))

list_A = [2, 3, 4]
list_B = [5, 6, 7]

#23*. Raise each list number to the corresponding number on another list:
new_lst = map(lambda x, y: x + y, list_A, list_B)
print(list(new_lst))

#24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
new_lst_to_sort = filter(lambda element: element % 2 == 1, lst_to_sort)
print(list(new_lst_to_sort))

#25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
lst_neg_number = filter(lambda element: element < 0, range(-10, 10))
print(list(lst_neg_number))

#26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]

def compare_list(lst1, lst2):
	def compare_elemets(v):
		if (v in lst1):
			return True
		else:
			return False
	filtered = filter(compare_elemets, lst2)
	print(f'The filtered letters are:{list(filtered)}')

compare_list(list_1, list_2)
