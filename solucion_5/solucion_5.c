#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

#define ROWS 1000
#define COLS 1000
#define DENSITY 0.1

void generate_sparse_matrix(int rows, int cols, float density, double **matrix) {
    int i, j;
    srand(time(NULL));
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            if ((rand() / (float) RAND_MAX) < density) {
                matrix[i][j] = rand() % 100;
            } else {
                matrix[i][j] = 0;
            }
        }
    }
}

void multiply_matrices(int rowsA, int colsA, int colsB, double **A, double **B, double **C) {
    int i, j, k;
    #pragma omp parallel for private(i, j, k) shared(A, B, C)
    for (i = 0; i < rowsA; i++) {
        for (j = 0; j < colsB; j++) {
            C[i][j] = 0;
            for (k = 0; k < colsA; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    double **A = (double **)malloc(ROWS * sizeof(double *));
    double **B = (double **)malloc(COLS * sizeof(double *));
    double **C = (double **)malloc(ROWS * sizeof(double *));

    if (A == NULL || B == NULL || C == NULL) {
        fprintf(stderr, "Error al asignar memoria.\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < ROWS; i++) {
        A[i] = (double *)malloc(COLS * sizeof(double));
        C[i] = (double *)malloc(COLS * sizeof(double));
        if (A[i] == NULL || C[i] == NULL) {
            fprintf(stderr, "Error al asignar memoria.\n");
            exit(EXIT_FAILURE);
        }
    }
    for (int i = 0; i < COLS; i++) {
        B[i] = (double *)malloc(ROWS * sizeof(double));
        if (B[i] == NULL) {
            fprintf(stderr, "Error al asignar memoria.\n");
            exit(EXIT_FAILURE);
        }
    }

    generate_sparse_matrix(ROWS, COLS, DENSITY, A);
    generate_sparse_matrix(COLS, ROWS, DENSITY, B);

    multiply_matrices(ROWS, COLS, ROWS, A, B, C);

    printf("Multiplicación de matrices completada.\n");
    // Descomentar para imprimir la matriz resultante
    // for (int i = 0; i < ROWS; i++) {
    //     for (int j = 0; j < ROWS; j++) {
    //         printf("%f ", C[i][j]);
    //     }
    //     printf("\n");
    // }

    // Liberar memoria
    for (int i = 0; i < ROWS; i++) {
        free(A[i]);
        free(C[i]);
    }
    for (int i = 0; i < COLS; i++) {
        free(B[i]);
    }
    free(A);
    free(B);
    free(C);

    return 0;
}
