def verify(isbn):

    try:
        s = isbn.replace('-', '')
        l = [10 if n[1] == 'X' and n[0] == (len(s) - 1) else int(n[1]) for n in enumerate(s)]
        #creates a list of isbn values, if value is an X AND is last element of isbn, replaces it with 10, otherwise returns an error
    except:
        return False

    return len(l) == 10 and sum([l[abs(n-10)] * n for n in range(10,0,-1)]) % 11 == 0
    #first checks that the isbn is of correct lenght then applies the formula to check if correct isbn
