import numpy as np
from scipy.sparse import random, csr_matrix

n_rows, n_cols = 1000, 1000
density = 0.1

A = random(n_rows, n_cols, density=density, format='csr', dtype=np.float64)
B = random(n_rows, n_cols, density=density, format='csr', dtype=np.float64)

C = A.dot(B)

print("Matriz C resultante de la multiplicación:")
print(f"Tamaño de C: {C.shape}")
print(C)
