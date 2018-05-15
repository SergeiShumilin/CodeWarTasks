def likes(names):
    if not names:
        s = 'no one likes this'
    elif len(names)==1:
        s = names[0]+" likes this"
    elif len(names)==2:
        s = names[0]+' and '+ 'like this'
    elif len(names) == 3:
        s = names[0] +', ' + names[1]+' and ' + names[2]+" like this"
    else:
        s = names[0]+', '+names[1]+' and '+ len(names)-2+ ' others like this'
    return 'must be ',s


