def partition(a, left, right):
    i=left-1
    pivot=a[right]
    for j in range (left, right):
        if a[j]<=pivot:
            i+=1
            a[i], a[j] = a[j], a[i]
    i+=1
    a[i], a[right]= a[right], a[i]
    return i
def quick_sort(a, left, right):
    if (left < right):
        p = partition(a, left, right)
        quick_sort(a,left,p-1)
        quick_sort(a,p+1, right)
a=[9,8,1,4,3,2,6,5,7,0]
n=len(a)
quick_sort(a, 0, n-1)
print(a)