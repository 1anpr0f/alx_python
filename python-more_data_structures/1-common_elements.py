def common_elements(set_1, set_2):
    for k, j in zip(sorted(set_1),sorted(set_2)):
        if k == j :
            print(list(k))