"""**Merge Sort**"""

def mergeSort(A, p, r):
    # Jika masih ada lebih dari satu elemen
	if p < r:
        # Temukan titik tengah
		q = p + (r - p) // 2

        # Panggil rekursif untuk bagian kiri dan kanan
		mergeSort(A, p, q)
		mergeSort(A, q + 1, r)
		merge(A, p, q, r)
	
def merge(A, p, q, r):
    # Hitung panjang dari dua bagian yang akan diurutkan
	n1 = q - p + 1
	n2 = r - q

    # Buat array temporer untuk bagian kiri dan kanan
	L = [0] * (n1)
	R = [0] * (n2)

    # Salin elemen ke array temporer
	for i in range(0, n1):
		L[i] = A[p + i]
	for j in range(0, n2):
		R[j] = A[q + 1 + j]

    # Gabungkan kembali dua bagian menjadi satu
	i = 0
	j = 0
	k = p

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
		k += 1

    # Salin sisa elemen jika ada
	while i < n1:
		A[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		A[k] = R[j]
		j += 1
		k += 1

A = [32, 12, 9, 18, 3, 21, 47, 26]
n = len(A)

mergeSort(A, 0, n - 1)  # Panggil fungsi Merge Sort
print("Sorted array is")
for i in range(n):
    print(A[i], end=" "),
