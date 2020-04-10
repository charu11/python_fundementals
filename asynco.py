def find_divisibles(inrange, div_by):
    print('finding the nums in range {} divisible by {}'.format(inrange, div_by))
    located = []

    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)


