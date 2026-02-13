def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if (a[j]>a[j+1]):
                a[j], a[j+1]= a[j+1],a[j]
a=[9,8,1,4,3,2,6,5,7,0]
bubble_sort(a)
print(a)