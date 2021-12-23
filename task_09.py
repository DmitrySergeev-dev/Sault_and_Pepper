def connect_dicts(dict1, dict2):
    # block of filtering initial dictionaries to del values<10
    d1_res = {key: value for key, value in dict1.items() if value > 10}
    d2_res = {key: value for key, value in dict2.items() if value > 10}
    # concate dictionaries according aims of task
    if sum(dict1.values()) > sum(dict2.values()):
        res = d2_res.copy()
        res.update(d1_res)
    else:
        res = d1_res.copy()
        res.update(d2_res)
    # Sort total dictionary
    sorted_res = {}
    sorted_keys = sorted(res, key=res.get)
    for val in sorted_keys:
        sorted_res[val] = res[val]
    print(sorted_res)


# TEST
connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5})
connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15})
connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15})
