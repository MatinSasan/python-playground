lambda x: x > 5

#  equals to:


def lambda1(x):
    return x > 5


def alter(values, check):
    return [val for val in values if check(val)]
    # return list(filter(check, values))


def remove_numbers(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)])


def skip_letter(value, letter):
    return alter(value, lambda x: x != letter)


my_list = [1, 2, 3, 4, 5]
another_list = alter(my_list, lambda x: x != 5)

print(another_list)

print(remove_numbers('progr3ammer'))


print(skip_letter("coding", 'i'))
