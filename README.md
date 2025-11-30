# TikTok Analytics Bot (Simulasi)

File utama: `uts_trans_digital.py`  
Versi: v1.0 (Simulasi, manual data collection)

Script ini mensimulasikan proses **analisis sederhana akun TikTok kampus** untuk keperluan tugas UTS.  
Script **tidak benar-benar terhubung ke TikTok**, melainkan menggunakan data yang diambil secara manual dari akun sosmed perguruan tinggi / universitas.

---

## 1. Tujuan Aplikasi

Aplikasi ini dibuat untuk mensimulasikan:

1. **Pencarian akun resmi** berdasarkan kata kunci (nama universitas).
2. **Pengambilan konten (scraping simulasi)** dari setiap akun yang ditemukan.
3. **Perhitungan rata-rata interaksi** (like, share, komentar) per akun.
4. **Analisis engagement**:
   - Menentukan akun dengan **engagement tertinggi**.
   - Menentukan akun yang **paling aktif secara interaksi** (berdasarkan rata-rata komentar).
5. **Pembuatan laporan otomatis** dalam bentuk:
   - File Excel (`.xlsx`)
   - File CSV
   - File teks (`Laporan_Otomatis.txt`)

Semua dijalankan secara otomatis melalui satu file Python.

---

## 2. Fitur Utama Script

### 2.1 Simulasi Pencarian Akun TikTok

Fungsi: `search_tiktok_accounts(keywords)`

- Input: list kata kunci, misalnya:
  ```python
  search_keywords = ["universitas indonesia", "ugm", "itb", "unpad", "binus"]
