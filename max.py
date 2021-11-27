def max (a):
    max = a[0]
    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
    return(max)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max(a)