__author__ = 'Tramel Jones'

def median(a,b,c):
    if a>b:
        if c>a:
            return a
    elif b>c: #Assume that b > a
        return max(a,c) #Assume b > a and b > c, making b the max value. Median is second place
    else:
        return b

def median2(a,b,c,min,max):
    return a^b^c^min^max
#X-clusive Or returns 0 for matches min & max
# 4, 67, 1, min=1, max=67 becomes 4^0^0^0^0 = 4

def main():
    print median(4,67,1)
    print median2(4,67,1,1,67)
    print median(5,7,9)
    print median2(5,7,9,5,9)
    print median(10,11,4)
    print median2(10,11,4,4,11)
    print median(5,4,6)
    print median2(5,4,6,4,6)

if __name__ == "__main__":
    main()