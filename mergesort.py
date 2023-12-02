"""**Merge Sort**"""

def mergeSort(A, p, r):
	if p < r:

		q = p+(r-p)//2

		mergeSort(A, p, q)
		mergeSort(A, q+1, r)
		merge(A, p, q, r)
	
def merge(A, p, q, r):
	n1 = q - p + 1
	n2 = r - q

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = A[p + i]

	for j in range(0, n2):
		R[j] = A[q + 1 + j]

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

	while i < n1:
		A[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		A[k] = R[j]
		j += 1
		k += 1

A = [32, 12, 9, 18, 3, 21, 47, 26 ]
n = len(A)

mergeSort(A, 0, n-1)
print("Sorted array is")
for i in range(n):
    print(A[i], end=" "),
