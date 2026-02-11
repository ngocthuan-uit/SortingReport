import numpy as np
import time
import sys
import matplotlib.pyplot as plt

dataset = []
for i in range(5):
    arr = np.random.uniform(-10000, 10000, 1000000)
    dataset.append(arr)
for i in range(5):
    arr = np.random.randint(-10000, 10000, 1000000)
    dataset.append(arr)
dataset[0] = np.sort(dataset[0])
dataset[1] = np.sort(dataset[1])[::-1]

def partition(a, left, right):
    i = left
    j = right
    pivot = a[(left+right)//2]
    while(True):
        while (a[i] < pivot):
            i += 1
        while (a[j] > pivot):
            j -= 1
        if (i < j):
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        else:
            return j
def quick_sort(a, left, right):
    if (left >= right):
        return
    p = partition(a, left, right)
    quick_sort(a, left, p)
    quick_sort(a, p+1, right)

def heapify(a, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if (left < n and a[left] > a[largest]):
        largest = left
    if (right < n and a[right] > a[largest]):
        largest = right
    if largest != i:
        a[largest], a[i] = a[i], a[largest]
        heapify(a, n, largest)
def heap_sort(a, n):
    for i in range (n//2-1, -1, -1):
        heapify(a, n, i)
    for i in range (n):
        a[0], a[n-i-1] = a[n-i-1], a[0]
        heapify(a, n-i-1, 0)

def merge(a, left, right, mid):
    left_arr = a[left : mid+1].copy()
    right_arr = a[mid+1 : right+1].copy()
    i = j = 0
    k = left
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            a[k] = left_arr[i]
            i += 1
            k += 1
        else:
            a[k] = right_arr[j]
            j += 1
            k += 1
    while i < len(left_arr):
        a[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        a[k] = right_arr[j]
        j += 1
        k += 1
def merge_sort(a, left, right):
    if left < right:
        mid = (left + right)//2
        merge_sort(a, left, mid)
        merge_sort(a, mid+1, right)
        merge(a, left, right, mid)

def numpy_sort(a):
    return np.sort(a)

def run_experiment():
    algorithms = ["QuickSort", "HeapSort", "MergeSort", "NumpySort"]
    results = {name: [] for name in algorithms}
    for index, data in enumerate(dataset):
        arr = data.copy()
        start = time.time()
        quick_sort(arr, 0, len(arr)-1)
        results["QuickSort"].append((time.time() - start)*1000)
        arr = data.copy()
        start = time.time()
        heap_sort(arr, len(arr))
        results["HeapSort"].append((time.time() - start)*1000)
        arr = data.copy()
        start = time.time()
        merge_sort(arr, 0, len(arr)-1)
        results["MergeSort"].append((time.time() - start)*1000)
        arr = data.copy()
        start = time.time()
        numpy_sort(arr)
        results["NumpySort"].append((time.time() - start)*1000)
    return results
def plot(results):
    x = np.arange(1, 11) 
    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - 0.3, results["QuickSort"], 0.2, label='QuickSort', color='#4472C4')
    ax.bar_label(rects1, fmt='%.0f', padding=2, fontsize=8)
    rects2 = ax.bar(x - 0.1, results["HeapSort"], 0.2, label='HeapSort', color='#ED7D31')
    ax.bar_label(rects2, fmt='%.0f', padding=2, fontsize=8)
    rects3 = ax.bar(x + 0.1, results["MergeSort"], 0.2, label='MergeSort', color='#A5A5A5')
    ax.bar_label(rects3, fmt='%.0f', padding=2, fontsize=8)
    rects4 = ax.bar(x + 0.3, results["NumpySort"], 0.2, label='NumPySort', color='#FFC000')
    ax.bar_label(rects4, fmt='%.0f', padding=2, fontsize=8)
    ax.set_ylabel('Thời gian thực hiện (ms)')
    ax.set_title('Kết quả thử nghiệm trên bộ dữ liệu')
    ax.set_xticks(x)
    ax.legend()
    plt.tight_layout()
    plt.show()

results = run_experiment()
plot(results)


 