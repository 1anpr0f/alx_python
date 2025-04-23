def common_elements(set_1, set_2):
    for word1, word2 in zip(sorted(set_1),sorted(set_2)):
        if word1== word2 :
            return list(word1)
        else:
            return list()