def heapify(a, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if (left < n and a[largest] < a[left]):
        largest = left
    if (right < n and a[largest] < a[right]):
        largest = right
    if (largest != i):
        a[largest], a[i] = a[i], a[largest]
        heapify(a, n, largest)
def heap_sort(a, n):
    for i in range (n//2-1 , -1, -1):
        heapify(a, n, i)
    for i in range (n):
        a[0], a[n-i-1] = a[n-i-1], a[0]
        heapify(a, n-i-1, 0)
a=[3,4,9,8,7,6]
n=len(a)
heap_sort(a, n)
print(a)

