def sort_list(list):
    try:
        # find max and min values in array
        el_max = max(list)
        el_min = min(list)

        # create arrays to keep indexes of all max and min values
        lst_max_index = []
        lst_min_index = []

        # find all indexes of el_max and el_min in array
        for i, el in enumerate(list):
            if el == el_max:
                lst_max_index.append(i)
            if el == el_min:
                lst_min_index.append(i)

        # replace max and min values to each other
        for i in lst_min_index:
            list[i] = el_max

        for i in lst_max_index:
            list[i] = el_min

        # add el_min in the end of array
        list.append(el_min)
        return (list)

    except ValueError:
        return (list)


# TEST
# sort_list([])
# sort_list([2, 4, 6, 8])
# sort_list([1])
# sort_list([1, 2, 1, 3])
