correct_combo = (3, 6, 1)

for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if(c1, c2, c3) == correct_combo:
                print('found the combo:{}'.format((c1, c2, c3)))


# in the above loop, even the right combo was found it continues to iterate. so it should be stopped


found_combo = False
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == correct_combo:
                print('found the corect combo:{}'.format((c1, c2, c3)))
                found_combo = True
                break