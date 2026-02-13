def merge(a, left, right, mid):
    left_arr=a[left : mid+1]
    right_arr=a[mid +1: right +1]
    i=j=0
    k=left
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i]<=right_arr[j]:
            a[k]=left_arr[i]
            k+=1
            i+=1
        else:
            a[k]=right_arr[j]
            k+=1
            j+=1
    while (i<len(left_arr)):
        a[k]=left_arr[i]
        k+=1
        i+=1
    while (j<len(right_arr)):
        a[k]=right_arr[j]
        k+=1
        j+=1
def merge_sort(a, left, right):
    if left<right:
        mid=(left+right)//2
        merge_sort(a, left, mid)
        merge_sort(a, mid+1, right)
        merge(a, left, right, mid)
a=[9,8,1,4,3,2,6,5,7,0]
n=len(a)
merge_sort(a, 0, n-1)
print(a)