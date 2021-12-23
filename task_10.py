def count_words(string):
    string_filtered = "".join([sym for sym in string.lower() if sym.isalpha() or sym == " "])
    lst = string_filtered.split()
    uniq_words = set(lst)
    counters = []
    for el in uniq_words:
        counters.append(lst.count(el))
    res = dict(zip(uniq_words, counters))
    print(res)


# TEST
count_words("A man, a plan, a canal -- Panama")
count_words("Doo bee doo bee doo")
