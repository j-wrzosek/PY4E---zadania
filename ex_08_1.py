numerki = [1,3,4,5,6,7]
lista = []
def chop(t):
    del t[0],
    del t[-1],
    print(t)
    return None

chop(numerki)


numerki2 = [3,4,5,6]
def middle(y):
    return y[1:-1]


print(middle(numerki2))
