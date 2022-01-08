def coincidence(list=[], range=range(0)):
    """Verifies if number in range"""
    num_lst = []
    lst_range = [num for num in range]
    for el in list:
        if type(el) in [int, float]:
            if lst_range[0] <= el <= lst_range[-1]:
                num_lst.append(el)
        else:
            continue
    return (num_lst)


#  TEST
# coincidence([1, 2, 3, 4, 5], range(3, 6))
# coincidence()
# coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))
