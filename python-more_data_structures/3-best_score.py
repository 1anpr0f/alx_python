def best_score(a_dictionary):
    if not a_dictionary:
        return None
    z = 0
    best_key = None
    for k,v in a_dictionary.items():
        if v > z:
            z = v
            best_key = k
    return  "{}".format(best_key) if best_key != None else None
    
        