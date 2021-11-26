def max (a):
    max = a[0]
    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
    return(max)