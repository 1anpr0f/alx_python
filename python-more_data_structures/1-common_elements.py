def common_elements(set_1, set_2):
    for k, j in zip(set_1,set_2):
        if k == j :
            print(list(k))