def common_elements(set_1, set_2):
    empty_list = []
    for word1 in set_1:
        for word2 in set_2:
            if word1== word2 :
                empty_list.append(word1)
                print(empty_list)
            else:
                print(empty_list)