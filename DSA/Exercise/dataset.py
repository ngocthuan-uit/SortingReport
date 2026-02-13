import numpy as np
np.random.seed(42)
with open('dataset_full.txt', 'wb') as f:
    for i in range(5):
        arr = np.random.uniform(-10000, 10000, 1000000)
        if i == 0:
            arr.sort()
        elif i == 1:
            arr = -np.sort(-arr)
        np.savetxt(f, arr, fmt='%.6f')
    for _ in range(5):
        arr = np.random.randint(-10000, 10000, 1000000)
        np.savetxt(f, arr, fmt='%d')