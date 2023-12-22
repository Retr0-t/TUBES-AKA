"""**Quick Sort**"""

import numpy as np
from random import shuffle

def partition(arr, left_index):
    # Membagi array menjadi bagian kiri dan kanan
    left_part = arr[:left_index]
    right_part = arr[left_index:]

    # Jika bagian kiri memiliki lebih dari satu elemen, lakukan pengurutan Quick Sort
    if len(left_part) > 1:
        quick_sort(left_part)
    
    # Jika bagian kanan memiliki lebih dari satu elemen, lakukan pengurutan Quick Sort
    if len(right_part) > 1:
        quick_sort(right_part)

def quick_sort(arr):
    last_index = len(arr) - 1
    
    pivot = arr[last_index]

    left_index = -1
    right_index = 0

    while left_index < right_index:
        # Cari elemen dari kiri yang lebih besar dari pivot
        left_index = last_index
        for index in range(last_index):
            if arr[index] > pivot:
                left_index = index
                break

        # Cari elemen dari kanan yang lebih kecil dari pivot
        right_index = -1
        for index in range(last_index - 1, -1, -1):
            if arr[index] < pivot:
                right_index = index
                break

        # Tukar elemen jika indeks kiri lebih besar dari indeks kanan
        if left_index > right_index:
            arr[left_index], arr[last_index] = arr[last_index], arr[left_index]
        else:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]

    # Rekursif bagi array berdasarkan indeks yang ditemukan
    partition(arr, left_index)

# Buat array berisi 0 sampai 999 dan acak isi array
random_array = np.arange(10)
shuffle(random_array)

print(random_array)

quick_sort(random_array)  # Panggil fungsi Quick Sort
