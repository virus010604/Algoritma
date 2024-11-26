import random

# Mengatur random seed
random.seed(42)

# Generate 50 angka acak dari 0 s/d 100
data = [random.randint(0, 100) for _ in range(50)]
print("Data sebelum sorting:", data)

# Fungsi Merge Sort menggunakan metode Divide & Conquer
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Gabungkan dua subarray
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

    return data

# Sorting menggunakan metode Divide & Conquer
sorted_data = merge_sort(data.copy())
print("Data setelah sorting (Divide & Conquer):", sorted_data)
