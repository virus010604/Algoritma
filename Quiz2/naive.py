import random
import numpy as np

# Mengatur random seed
random.seed(42)

# Generate 50 angka acak dari 0 s/d 100
data = [random.randint(0, 100) for _ in range(50)]
print("Data sebelum sorting:", data)

# Fungsi Naive Bayes untuk menghitung probabilitas angka
def naive_bayes_sort(data):
    # Hitung probabilitas kemunculan angka
    unique, counts = np.unique(data, return_counts=True)
    probabilities = dict(zip(unique, counts / len(data)))
    print("Probabilitas setiap angka:", probabilities)
    return sorted(data)

# Sorting menggunakan pendekatan probabilitas
sorted_data = naive_bayes_sort(data)
print("Data setelah sorting (Naive Bayes):", sorted_data)
