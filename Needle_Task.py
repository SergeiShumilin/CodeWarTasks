arr = ['hay', 'needle', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']
def find_needle(haystack):
    for hay in range(len(haystack)):
        if haystack[hay]=='needle':
            print('found the needle at position', hay)


find_needle(arr)