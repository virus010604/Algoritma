# Algoritma

**Name:** Juan P Kuganda

**Student ID:** F55123061 <br>

**Kelas:** Informatika B


<hr>
<h2>Quiz 2</h2>
<p>Naive Bayes Method
Metode Naive Bayes pada implementasi sorting di atas sebenarnya tidak menggunakan algoritma Naive Bayes dalam pengertian klasifikasi penuh, tetapi hanya menghitung probabilitas kemunculan elemen dalam dataset. Proses sorting dilakukan menggunakan fungsi bawaan Python, yaitu sorted(), yang menerapkan algoritma Timsort. Pada kasus terbaik (best case), jika data sudah terurut sebelumnya, algoritma Timsort hanya akan memindai data dan mengidentifikasi bahwa tidak ada perubahan yang diperlukan. Hal ini membuat kompleksitas waktu menjadi O(n) karena hanya memerlukan satu kali iterasi untuk memeriksa data.
<br>
Merge Sort (Divide & Conquer)
Merge Sort adalah algoritma Divide & Conquer yang membagi dataset menjadi dua bagian secara rekursif hingga tersisa elemen tunggal, lalu menggabungkannya kembali dengan urutan yang benar. Pada kasus terbaik (best case), data sudah terurut. Namun, karena sifat Merge Sort yang selalu membagi dan menggabungkan elemen, ia tetap memerlukan proses penggabungan semua subarray. Oleh karena itu, kompleksitas waktu untuk kasus terbaik tetap O(n log n), tanpa ada pengurangan langkah karena sifat algoritmanya yang tidak bergantung pada urutan awal data.
<br>
Perbandingan
Naive Bayes (menggunakan Timsort) lebih efisien dalam kasus terbaik dengan kompleksitas waktu O(n) jika data sudah terurut.
Merge Sort tetap memiliki kompleksitas waktu O(n log n) pada semua kasus, termasuk kasus terbaik, karena pembagian dan penggabungan data tetap dilakukan.
Hasil ini menunjukkan bahwa Timsort lebih unggul untuk kasus data yang sudah terurut, sedangkan Merge Sort lebih cocok untuk dataset dengan urutan acak atau tidak diketahui.</p>

