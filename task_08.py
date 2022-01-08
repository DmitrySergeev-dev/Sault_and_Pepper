def multiply_numbers(inputs=None):
    msg = 'None'
    # what if function was run without arguments
    if inputs is None:
        return msg
    lst = []  # total list
    # what if inputs is float
    if type(inputs) == float:
        inputs = str(inputs).replace('.', '')
        for el in inputs:
            lst.append(int(el))
    else:
        for el in inputs:
            try:
                lst.append(int(el))
            except (TypeError, ValueError):
                continue
    # what if argument was without any digits
    if len(lst) == 0:
        return msg
    res = 1
    for el in lst:
        res *= el
    return (res)


# # TEST
# multiply_numbers()
# multiply_numbers('ss')
# multiply_numbers('1234')
# multiply_numbers('sssdd34')
# multiply_numbers(2.3)
# multiply_numbers([5, 6, 4])
