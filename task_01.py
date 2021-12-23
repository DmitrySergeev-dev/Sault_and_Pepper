def is_palindrome(string):
    """Verifies if string is palindrom"""
    str_string = str(string)
    lst = []
    for el in str_string.lower():
        if el.isalpha():
            lst.append(el)
    print(lst == lst[::-1])


# TEST
is_palindrome("A man, a plan, a canal -- Panama")
is_palindrome("Madam, I'm Adam!")
is_palindrome(333)
is_palindrome(None)
is_palindrome("Abracadabra")
