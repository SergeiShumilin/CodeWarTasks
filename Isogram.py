# my version
def is_isogram(string):
    string = string.lower()
    for i in string:
        j = string.count(i)
        if j > 1:
            return False
    return True


# how it could be
is_isogram = lambda s: len(set(s.lower())) == len(s)

print(is_isogram('eerc'))