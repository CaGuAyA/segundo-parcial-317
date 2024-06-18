import numpy as np
from scipy.sparse import random, csr_matrix
from multiprocessing import Pool, cpu_count, get_start_method

def multiplicar_matrices(A, B):
    return A.dot(B)

def parallel_multiplication(A, B):
    num_processes = cpu_count()
    pool = Pool(processes=num_processes)
    result = pool.apply(multiplicar_matrices, args=(A, B))
    pool.close()
    pool.join()
    return result

if __name__ == '__main__':
    filas = 1000
    columnas = 1000

    A = random(filas, columnas, density=0.1, format='csr')
    B = random(columnas, filas, density=0.1, format='csr')

    try:
        method = get_start_method()
        print(f"Using start method: {method}")
    except AttributeError:
        pass

    C = parallel_multiplication(A, B)
    print("Multiplicación de matrices dispersas completada.")
    print(C)