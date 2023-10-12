def merge_list(l1, l2):
    for i in range(len(l1)):
        check = isinstance(l1[i],int)
        if (check == False):
            raise TypeError
    for i in range(len(l2)):
        check = isinstance(l2[i],int)
        if (check == False):
            raise TypeError
    
    l3 = l1 + l2
    for i in range(0,len(l3)):
         for j in range(i+1, len(l3)):
            if l3[i] >= l3[j]:
                l3[i], l3[j] = l3[j],l3[i]
    return l3
