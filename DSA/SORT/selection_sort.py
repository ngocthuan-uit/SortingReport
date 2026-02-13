def SelectionSort(a, n):
    for i in range (n-1):
        min = i
        for j in range (i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
a=[9,8,1,4,3,2,6,5,7,0]
n=len(a)
SelectionSort(a, n)
print(a)

