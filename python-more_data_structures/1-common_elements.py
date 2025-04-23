def common_elements(set_1, set_2):
    set_1 = sorted(list(set_1))
    set_2 = sorted(list(set_1))
    for k, j in zip(set_1,set_2):
        if k == j :
            print(list(k))