def max_odd(array):
    """Return max odd number from array """
    lst_num = list(filter(lambda el: type(el) in [int, float], array))
    lst_res = []
    for el in array:
        if type(el) in [int, float]:
            if int(el) % 2 != 0:
                lst_res.append(int(el))
    if len(lst_res) != 0:
        return (max(lst_res))
    else:
        return None

# TEST
# max_odd([1, 2, 3, 4, 4])
# max_odd([21.0, 2, 3, 4, 4])
# max_odd(['ololo', 2, 3, 4, [1, 2], None])
# max_odd(['ololo', 'fufufu'])
# max_odd([2, 2, 4])
