import time
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# Contoh pengujian
X = [1, 5, 6, 4, 3, 3, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sorted_X_quick = quick_sort(X.copy())
start_time = time.perf_counter()
print("Quick Sort Result:", sorted_X_quick)
end_time = time.perf_counter()
print("Execution Time:", end_time-start_time)


# Setelah melakukan pengujian di dapati
# bahwa quicksort mengeksekusi lebih cepat dibandingkan dengan
# algoritma merge_sort


# Worst Case: O(n²)
# Terjadi jika pivot dipilih buruk, seperti array sudah terurut (ascending/descending), sehingga pembagian tidak merata.
# Best Case: O(n log n)
# Ketika pivot membagi array menjadi dua bagian yang seimbang di setiap iterasi.
# Average Case: O(n log n)
# Dalam rata-rata pembagian data mendekati setara, menghasilkan kinerja optimal.

