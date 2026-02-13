def insertion_sort(a,n):
    for i in range (1, n):
        temp = a[i]
        j = i-1
        while (j >= 0 and temp < a[j]):
            a[j+1] = a[j]
            j-=1
        a[j+1] = temp
a = list(map(int,input().split()))
#a=[9,8,1,4,3,2,6,5,7,0]
n=len(a)
insertion_sort(a, n)
print(a)
