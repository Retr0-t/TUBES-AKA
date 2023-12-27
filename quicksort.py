import random  # Tambahkan baris ini untuk mengimport modul random

def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index)
        quick_sort(arr, partition_index + 1, high)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

# Buat array berisi 0 sampai 9 dan acak isi array
random_array = list(range(10))
random.shuffle(random_array)  # Menggunakan fungsi shuffle dari modul random

print("Sebelum pengurutan:")
print(random_array)

quick_sort(random_array, 0, len(random_array) - 1)  # Panggil fungsi Quick Sort

print("Setelah pengurutan:")
print(random_array)
