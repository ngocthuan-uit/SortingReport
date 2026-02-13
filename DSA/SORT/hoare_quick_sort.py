def partition(a, left, right):
    i=left
    j=right
    pivot = a[left]
    while(True):
        while (a[i]<pivot):
            i+=1
        while (a[j]>pivot):
            j-=1
        if (i<j):
            a[i], a[j] = a[j], a[i]
            i+=1 
            j-=1
        else:
            return i
def quick_sort(a, left, right):
    if left>=right:
        return
    p=partition(a,left,right)
    quick_sort(a,left,p)
    quick_sort(a,p+1,right)
a=[3,4,9,8,7,6]
n=len(a)
quick_sort(a, 0, n-1)
print(a)