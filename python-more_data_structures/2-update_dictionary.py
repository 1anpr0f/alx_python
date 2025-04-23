def update_dictionary(a_dictionary, key, value):
    a_dictionary[str(key)]= str(value)
    for k,v in a_dictionary.items():
        print(f"{k}:{v}")