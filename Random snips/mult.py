def multMain(x, y):
    neg = x < 0 or y < 0
    low = min(abs(x), abs(y))
    return negMult(x, y, low) if neg else mult(x, y, low)  ##return neg? mult: negmult
def mult(x, y, low):
    high = max(x,y)
    if y == 0 or x == 0:
        return 0
    elif low == 1:
        return high
    return high + mult(x, y, low-1)
def negMult(x, y, low):
    if x < 0 and y < 0:
        return mult(abs(x), abs(y), low)
    return -1* mult(abs(x), abs(y), low)
