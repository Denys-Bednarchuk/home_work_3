import functools

# 1
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
# 140277406453808
print(id(str_b))
# 140707058945520
print(id(set_c))
# 140220223300096
print(id(lst_d))
# 140008994345856
print(id(dict_e))
# 140673069769408

# 2
lst_d.extend([4, 5])
print(id(lst_d))
# 140099171525504

# 3
print(type(int_a))  # <class 'int'
print(type(str_b))  # <class 'str'
print(type(set_c))  # <class 'set'
print(type(lst_d))  # <class 'list'
print(type(dict_e))  # <class 'dict'

# 4
print(isinstance(int_a, int))  # True
print(isinstance(str_b, str))  # True
print(isinstance(set_c, set))  # True
print(isinstance(lst_d, list))  # True
print(isinstance(dict_e, dict))  # True

# 5
print("Anna has {} apples and {} peaches.".format(5, 6))
# Anna has 5 apples and 6 peaches

# 6
print("Anna has {0} apples and {1} peaches.".format(5, 6))
# Anna has 5 apples and 6 peaches

# 7
print("Anna has {five} apples and {six} peaches.".format(five=5, six=6))
# Anna has 5 apples and 6 peaches

# 8
print("Anna has {0:5} apples and {1:3} peaches.".format(5, 6))
# Anna has     5 apples and   6 peaches

# 9
a = 5
p = 6
print(f"Anna has {a} apples and {p} peaches.")
# Anna has 5 apples and 6 peaches

# 10
a = 5
p = 6
print("Anna has %d apples and %d peaches." % (a, p))
# Anna has 5 apples and 6 peaches

# 11
a = 5
p = 6
anna_dict = {'five': a, 'six': p}
print("Anna has %(five)d apples and %(six)d peaches." % anna_dict)
# Anna has 5 apples and 6 peaches

# 12
lst_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_comp)
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

# 14
dict_comprehension = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comprehension)
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15
dict_comprehension = {d: d ** 2 if d % 2 == 1 else d // 0.5 for d in range(1, 11)}
print(dict_comprehension)
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

# 16
x = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        x[num] = num ** 3
print(x)
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# 17
x = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        x[num] = num ** 3
    else:
        x[num] = num
print(x)
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

# 18
foo = lambda x, y: x if x < y else y
print(foo)


# 19
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo)

# 20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
# [1, 5, 13, 15, 18, 24, 33, 55]

# 21
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort, reverse=True))
# [55, 33, 24, 18, 15, 13, 5, 1]

# 22
print(list(map(lambda x: x * 2, lst_to_sort)))

# 23
list_a = [2, 3, 4]
list_b = [5, 6, 7]
list_c = []
list_c = (list_a[0] ** list_b[0], list_a[1] ** list_b[1], list_a[2] ** list_b[2])
print(list_c)
# (32, 729, 16384)

# 24
lst_sum = functools.reduce(lambda a, b: a + b, lst_to_sort)
print(lst_sum)
# 164

# 25
print(list(filter(lambda x: (x % 2 == 1), lst_to_sort)))
# [5, 1, 33, 15, 13, 55]

# 26
print(list(filter(lambda x: x < 0, range(-10, 10))))
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
cmn_lst = list(filter(lambda x: x in list_1, list_2))
print(cmn_lst)
# [2, 3, 5, 7]
