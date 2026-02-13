def binary_search(a, x):
    l=0
    r = len(a)-1
    while(l<=r):
        m=(l+r)//2
        if a[m]==x:
            return m
        elif a[m]>x:
            r=m-1
        else:
            l=m+1
    return -1
a=[1,5,7,8,10,11,42]
print(binary_search(a, 42))