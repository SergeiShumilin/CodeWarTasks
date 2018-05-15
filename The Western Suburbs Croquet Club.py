# Входные данные
data = [[45, 12], [55, 21], [19, -2], [104, 20]]


# Функция возвращающая список Senior\Open
def openOrSenior(data):
    result = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            result.append('Senior')
        else:
            result.append('Open')
    return result


print(openOrSenior(data))
