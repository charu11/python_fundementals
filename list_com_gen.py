x = (i for i in range(300000))
print(list(x)[:5])

y = [i for i in range(300000)]
print(y[:5])


# Generator example

input_list = [5, 6, 2, 1, 7, 10, 12]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xy = (i for i in input_list if div_by_five(i))
print(list(xy))

# list comprehension
yz = [i for i in input_list if div_by_five(i)]
print(yz)
