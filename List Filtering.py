# my version
def filter_list(l):
    res = []
    for i in l:
        if type(i) is int:
            res.append(i)
    return res


# how it could be
def filter_list(l):
    return [i for i in l if type(i) is int]


r = [1, 4, 5, 1, '12e', '14']
print(filter_list(r))
