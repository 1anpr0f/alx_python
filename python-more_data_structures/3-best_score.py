def best_score(a_dictionary):
    z = None
    for k,v in a_dictionary:
        if v > z:
            z = v
    return  "{}".format(k)
    
        