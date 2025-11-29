# TikTok Analytics Bot (Simulasi)

Script Python ini mensimulasikan proses **pencarian akun kampus di TikTok**, melakukan **“scraping” konten secara fiktif**, lalu menyusun **laporan analisis engagement** dalam bentuk **Excel, CSV, dan file teks**.

> ⚠️ Catatan penting:  
> Script **tidak** terhubung ke API TikTok asli. Seluruh data (akun, konten, likes, komentar, dsb.) adalah **data dummy/simulasi** yang dibuat untuk keperluan demo.

---

## Fitur Utama

1. **Simulasi pencarian akun TikTok**
   - Mencari akun berdasarkan daftar `keywords` (misalnya: *"universitas indonesia"*, *"ugm"*, *"itb"*, dll).
   - Hanya akun yang **verified** yang akan diproses lebih lanjut.
   - Menampilkan log proses scanning dengan efek delay seperti sedang memanggil API.

2. **Simulasi scraping konten**
   - Mengambil `num_posts` (default: 10) postingan terbaru secara simulasi.
   - Menghasilkan data:
     - Nama akun
     - Jumlah follower
     - Tanggal unggahan
     - Judul/keterangan video
     - Jumlah like, share, komentar
     - Contoh komentar (sample) yang diambil secara acak

3. **Perhitungan engagement sederhana**
   - Menghitung rata-rata:
     - `Jumlah Like`
     - `Jumlah Share`
     - `Jumlah Komentar`
   - Menghitung `Total Engagement` per akun dan mengurutkan dari yang tertinggi.

4. **Export hasil otomatis**
   - Menyimpan data detail ke:
     - `Hasil_Scan_TikTok.xlsx`
     - `Hasil_Scan_TikTok.csv`
   - Membuat laporan ringkas ke:
     - `Laporan_Otomatis.txt`

---

## Teknologi & Library

- Python 3.8+ (disarankan)
- [pandas](https://pandas.pydata.org/) (untuk pengolahan data tabular)
- Library standar Python:
  - `random`
  - `time`
  - `sys`
  - `datetime`

---

## Instalasi

1. **Clone / salin proyek ini** (atau simpan file `.py` di folder kerja Anda).

2. **Buat virtual environment (opsional tapi direkomendasikan)**

   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   # atau
   venv\Scripts\activate         # Windows
