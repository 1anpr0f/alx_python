def best_score(a_dictionary):
    z = 0
    for k,v in a_dictionary.items():
        if v > z:
            z = v
        return  "{}".format(k)
    
        