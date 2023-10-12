def reverse_sort_dictionary(d1):
    if (isinstance(d1,dict) != True):
        raise TypeError
    
    new_dict = []
    
    for i in range(len(d1)):
        name = (list(reversed(sorted(d1.keys()))))[i]
        number = (list(reversed(sorted(d1.items()))))[i][1][0]
        some_tuple = (name,number)
        new_dict.append(some_tuple)
    return new_dict
