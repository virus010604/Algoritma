import time
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Rekursi untuk membagi array
        merge_sort(left)
        merge_sort(right)

        # Proses penggabungan
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Menambahkan elemen yang tersisa
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
# Contoh pengujian
X = [1, 5, 6, 4, 3, 3, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sorted_X_merge = merge_sort(X.copy())
start_time = time.perf_counter()
print("Merge Sort Result:", sorted_X_merge)
end_time = time.perf_counter()
print("Execution Time:", end_time-start_time)


# Setelah melakukan pengujian di dapati
# bahwa quicksort mengeksekusi lebih cepat dibandingkan dengan
# algoritma merge_sort

# Merge Sort:
# Worst Case: O(n log n)
# Karena Merge Sort membagi array menjadi dua bagian setiap kali dan membutuhkan waktu O(n) untuk penggabungan.
# Best Case: O(n log n)
# Tidak ada perbedaan signifikan karena proses selalu sama.
# Average Case: O(n log n)
# Sama dengan best case dan worst case karena sifat rekursif dan penggabungan.
