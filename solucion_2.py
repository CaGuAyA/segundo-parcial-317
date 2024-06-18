import tkinter as tk
from tkinter import filedialog
import numpy as np
from PIL import Image
from scipy.sparse import csr_matrix

def load_images():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Seleccionar imágenes",
        filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")]
    )

    return list(file_paths)

def image_to_sparse_matrix(image_path):
    img_gray = Image.open(image_path).convert('L')
    width, height = img_gray.size
    pixels = np.array(img_gray.getdata(), dtype=np.uint8).reshape((height, width))
    
    sparse_pixels = csr_matrix(pixels)
    return sparse_pixels

image_paths = load_images()
print("Imágenes cargadas:", image_paths)

sparse_matrices = [image_to_sparse_matrix(image_path) for image_path in image_paths]

for i, sparse_matrix in enumerate(sparse_matrices):
    print(f"Matriz dispersa CSR de la imagen {i + 1}:")
    print(sparse_matrix)
