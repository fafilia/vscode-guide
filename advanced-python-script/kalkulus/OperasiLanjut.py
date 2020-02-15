def faktorial(a):
    if a>= 0 :
        if a <= 1 :
            return 1
        else:
            return (a* faktorial(a-1))

def jumlah(a):
    res = 0
    if a>= 0:
        for i in range (1,a+1):
            res += i 
    return res 