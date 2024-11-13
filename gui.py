import tkinter as tk  # Import modul Tkinter untuk membuat GUI

# Fungsi untuk menghasilkan hasil prediksi
def hasil_prediksi():
    # Mengubah teks label hasil_label menjadi "Prodi yang dipilih: Teknologi Informasi"
    hasil_label.config(text="Prodi yang dipilih: Teknologi Informasi")

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Judul jendela
root.geometry("400x600")  # Ukuran jendela (lebar x tinggi)

# Membuat label judul aplikasi
judul_label = tk.Label(
    root,  # Ditempatkan di jendela utama
    text="Aplikasi Prediksi Prodi Pilihan",  # Teks yang ditampilkan
    font=("Arial", 16, "bold")  # Font, ukuran, dan gaya (tebal)
)
judul_label.pack(pady=20)  # Menggunakan pack untuk meletakkan widget, dengan jarak vertikal (padding) 20 piksel

# List untuk menyimpan semua entry (input) nilai mata pelajaran
entry_list = []

# Membuat 10 input nilai mata pelajaran
for i in range(1, 11):  # Looping dari 1 sampai 10
    # Membuat frame sebagai wadah untuk label dan entry
    frame = tk.Frame(root)
    frame.pack(pady=5)  # Jarak antar frame sebesar 5 piksel
    
    # Membuat label untuk mata pelajaran
    label = tk.Label(
        frame,  # Ditempatkan di dalam frame
        text=f"Nilai Mata Pelajaran {i}: ",  # Menampilkan nomor mata pelajaran
        font=("Arial", 12)  # Ukuran font
    )
    label.pack(side=tk.LEFT)  # Meletakkan label di sisi kiri frame
    
    # Membuat entry (kotak input teks) untuk memasukkan nilai
    entry = tk.Entry(
        frame,  # Ditempatkan di dalam frame
        font=("Arial", 12),  # Ukuran font teks di dalam entry
        width=10  # Lebar kotak input
    )
    entry.pack(side=tk.LEFT)  # Meletakkan entry di sebelah kanan label
    
    # Menambahkan entry ke dalam list agar bisa diakses nanti
    entry_list.append(entry)

# Membuat tombol untuk menghasilkan hasil prediksi
prediksi_button = tk.Button(
    root,  # Ditempatkan di jendela utama
    text="Hasil Prediksi",  # Teks pada tombol
    command=hasil_prediksi,  # Fungsi yang dipanggil saat tombol ditekan
    font=("Arial", 12),  # Ukuran font
    bg="blue",  # Warna latar tombol
    fg="white"  # Warna teks tombol
)
prediksi_button.pack(pady=30)  # Jarak vertikal sebesar 30 piksel dari elemen sebelumnya

# Membuat label untuk menampilkan hasil prediksi
hasil_label = tk.Label(
    root,  # Ditempatkan di jendela utama
    text="",  # Awalnya tidak ada teks
    font=("Arial", 14),  # Ukuran font
    fg="green"  # Warna teks hijau
)
hasil_label.pack(pady=20)  # Jarak vertikal sebesar 20 piksel dari elemen sebelumnya

# Menjalankan loop utama Tkinter (event loop)
root.mainloop()

