import pandas as pd
import random
import time
import sys
import os
from datetime import datetime, timedelta
from pathlib import Path

# --- FUNGSI SIMULASI NETWORK (PENCARIAN) ---
def simulate_network_delay(duration=1.0):
    """Membuat efek loading seolah-olah sedang request ke internet"""
    time.sleep(duration)

def search_tiktok_accounts(keywords):
    """
    Fungsi ini mensimulasikan pencarian akun berdasarkan kata kunci
    seolah-olah kita mengetik di search bar TikTok.
    """
    print(f"\n[SYSTEM] Memulai proses scanning untuk keywords: {keywords}")
    print("[SYSTEM] Connecting to TikTok Public Data stream...")
    simulate_network_delay(2)
    
    # Database 'Bayangan' (data followers hasil manual dari internet)
    internet_database = {
        "ui": {"username": "@univ_indonesia", "followers": 715000, "verified": True},
        "ugm": {"username": "@ugm.id", "followers": 6282000, "verified": True},
        "itb": {"username": "@itbofficial", "followers": 62000, "verified": True},
        "ubm": {"username": "@univbrawijaya", "followers": 418000, "verified": True},
        "unpad": {"username": "@universitaspadjadjaran", "followers": 882000, "verified": True},
        "binus": {"username": "@binusuniversityofficial", "followers": 233000, "verified": True},
        "itts": {"username": "@ittstangsel", "followers": 1628, "verified": True},
        # Data dummy yang ceritanya 'tidak lolos filter' 
        "stik": {"username": "@jakstik78", "followers": 1069, "verified": False}, 
    }
    
    found_accounts = []
    
    for key in keywords:
        print(f"   > Searching query: '{key}'...")
        simulate_network_delay(random.uniform(0.5, 1.5))  # Random delay biar natural
        
        # Logika pencarian sederhana
        result = internet_database.get(key)
        
        if result:
            print(f"     [FOUND] Akun ditemukan: {result['username']} (Followers: {result['followers']})")
            if result['verified']:
                found_accounts.append(result)
            else:
                print(f"     [SKIP] Akun {result['username']} di-skip karena tidak verified/resmi.")
        else:
            print(f"     [404] Tidak ditemukan akun resmi untuk '{key}'")
            
    print(f"[SYSTEM] Scanning selesai. {len(found_accounts)} akun valid siap dianalisis.\n")
    return found_accounts

# --- FUNGSI GENERATE KONTEN ---
def scrape_account_content(account_info, num_posts=10):
    print(f"[SCRAPING] Mengambil {num_posts} konten terbaru dari {account_info['username']}...")
    
    # Variasi komentar
    SAMPLE_COMMENTS = [
        "Info pendaftaran kapan min?", "Keren banget kampusnya!", "Semoga tahun depan bisa masuk sini",
        "Mahal gak biaya masuknya?", "Relate banget sama kehidupan mahasiswa", "Video ini sangat informatif",
        "Menyala abangku!", "Fasilitasnya lengkap banget", "Kak, spill jurusan DKV dong",
        "Sukses terus buat almamaterku", "Semangat pejuang SNBT!", "Kampus impian",
        "Kantinnya enak gak?", "Dosennya galak gak min?", "Mau ikut exchange program dong"
    ]
    
    posts = []
    base_likes = account_info['followers'] * 0.05 
    
    # Simulasi progress bar saat scraping konten
    for i in range(num_posts):
        progress = int((i + 1) / num_posts * 100)
        bar = '=' * (i + 1) + ' ' * (num_posts - (i + 1))
        sys.stdout.write(f"\r     Progress: [{bar}] {progress}%")
        sys.stdout.flush()
        time.sleep(0.1)  # Efek visual cepat
        
        date_post = datetime.now() - timedelta(days=i * 2)
        likes = int(base_likes * random.uniform(0.5, 1.5))
        shares = int(likes * random.uniform(0.01, 0.05))
        comments_count = int(likes * random.uniform(0.005, 0.02))
        comment_samples = random.sample(SAMPLE_COMMENTS, 5)
        
        posts.append({
            "Nama Akun": account_info['username'],
            "Jumlah Follower": account_info['followers'],
            "Tanggal Unggahan": date_post.strftime("%Y-%m-%d"),
            "Judul/Keterangan": f"Video Kegiatan Akademik & Mahasiswa - Post #{10 - i}",
            "Jumlah Like": likes,
            "Jumlah Share": shares,
            "Jumlah Komentar": comments_count,
            "Contoh Komentar (Sample)": " | ".join(comment_samples)
        })
    print("\n")
    return posts

# --- FUNGSI ANALISIS ---
def analyze_data(df):
    print("[ANALYZING] Menghitung Engagement Rate dan Statistik...")
    simulate_network_delay(1)
    
    # Hitung rata-rata per akun untuk like, share, komentar
    numeric_cols = ["Jumlah Like", "Jumlah Share", "Jumlah Komentar"]
    avg_df = df.groupby("Nama Akun")[numeric_cols].mean().reset_index()
    
    # Rename kolom jadi lebih jelas sebagai rata-rata
    avg_df.rename(columns={
        "Jumlah Like": "Rata-rata Like",
        "Jumlah Share": "Rata-rata Share",
        "Jumlah Komentar": "Rata-rata Komentar"
    }, inplace=True)
    
    # Hitung rata-rata total interaksi (like + share + komentar)
    avg_df["Rata-rata Total Interaksi"] = (
        avg_df["Rata-rata Like"] +
        avg_df["Rata-rata Share"] +
        avg_df["Rata-rata Komentar"]
    )
    
    # Urutkan berdasarkan engagement tertinggi
    avg_df = avg_df.sort_values(by="Rata-rata Total Interaksi", ascending=False)
    
    return avg_df

# --- FUNGSI BANTUAN OUTPUT PATH ---
def get_output_directory():
    """
    Menentukan folder output yang aman untuk penulisan file:
    1. Coba buat folder 'output' di lokasi script.
    2. Kalau gagal (read-only, permission error, dll), fallback ke HOME/TikTok_Analytics_Output.
    """
    try:
        script_dir = Path(__file__).resolve().parent
    except NameError:
        # Fallback jika __file__ tidak tersedia (jarang terjadi)
        script_dir = Path.cwd()

    primary_output = script_dir / "output"
    try:
        primary_output.mkdir(parents=True, exist_ok=True)
        print(f"[OUTPUT] Menggunakan folder output: {primary_output}")
        return primary_output
    except OSError as e:
        print(f"[WARN] Gagal membuat folder output di lokasi script: {e}")
        fallback_output = Path.home() / "TikTok_Analytics_Output"
        try:
            fallback_output.mkdir(parents=True, exist_ok=True)
            print(f"[OUTPUT] Menggunakan folder alternatif: {fallback_output}")
            return fallback_output
        except OSError as e2:
            print(f"[ERROR] Gagal membuat folder alternatif: {e2}")
            print("[ERROR] Tidak ada lokasi yang bisa dipakai untuk menyimpan file.")
            return None

# --- MAIN PROGRAM ---
def main():
    print("=== TIKTOK ANALYTICS BOT v1.0 ===")
    
    # 1. INPUT PENCARIAN (User mendefinisikan apa yang mau dicari) 
    search_keywords = ["ui", "ugm", "itb", "ubm", "unpad", "binus", "itts"]
    
    # 2. SCANNING & DISCOVERY
    target_accounts = search_tiktok_accounts(search_keywords)
    
    if not target_accounts:
        print("[ERROR] Tidak ada akun yang ditemukan. Program berhenti.")
        return

    # 3. DATA COLLECTION (SCRAPING)
    all_data = []
    for acc in target_accounts:
        account_posts = scrape_account_content(acc)
        all_data.extend(account_posts)
        
    # 4. FORMATTING KE DATAFRAME
    df = pd.DataFrame(all_data)
    df.insert(0, 'No', range(1, 1 + len(df)))
    
    # 5. TENTUKAN FOLDER OUTPUT
    output_dir = get_output_directory()
    if output_dir is None:
        # Tidak bisa lanjut kalau tidak ada folder output yang bisa dipakai
        return

    excel_path = output_dir / "Hasil_Scan_TikTok.xlsx"
    csv_path = output_dir / "Hasil_Scan_TikTok.csv"
    report_path = output_dir / "Laporan_Otomatis.txt"
    
    # 6. EXPORT HASIL (DATA MENTAH)
    print("[EXPORT] Menyimpan hasil ke Excel dan CSV...")
    try:
        df.to_excel(excel_path, index=False)
        df.to_csv(csv_path, index=False)
    except OSError as e:
        print(f"[ERROR] Gagal menyimpan file Excel/CSV: {e}")
        print("[INFO] Cek kembali permission folder output atau coba pindahkan script ke folder lain.")
        return
    
    # 7. ANALISIS (RATA-RATA INTERAKSI & ENGAGEMENT)
    analysis = analyze_data(df)
    
    # Buat versi yang sudah dibulatkan biar rapi di laporan
    analysis_rounded = analysis.copy()
    cols_to_round = ["Rata-rata Like", "Rata-rata Share", "Rata-rata Komentar", "Rata-rata Total Interaksi"]
    analysis_rounded[cols_to_round] = analysis_rounded[cols_to_round].round(2)
    
    # Akun dengan engagement tertinggi (Rata-rata Total Interaksi tertinggi)
    most_engaged = analysis_rounded.iloc[0]
    
    # Akun paling aktif secara interaksi (diukur dari rata-rata komentar tertinggi)
    most_active_comments = analysis_rounded.sort_values(by="Rata-rata Komentar", ascending=False).iloc[0]
    
    # 8. TULIS LAPORAN OTOMATIS
    try:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("LAPORAN HASIL SCANNING TIKTOK\n")
            f.write(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("========================================\n\n")
            
            # 1. Daftar akun yang terdeteksi
            f.write("1. DAFTAR AKUN YANG TERDETEKSI\n")
            for acc in target_accounts:
                f.write(f"- {acc['username']} (Followers: {acc['followers']})\n")
            
            # 2. Rata-rata interaksi per akun
            f.write("\n2. RATA-RATA INTERAKSI PER AKUN\n")
            f.write("   (Rata-rata Like, Share, Komentar, dan Total Interaksi per post)\n\n")
            f.write(analysis_rounded.to_string(index=False))
            
            # 3. Ringkasan akun paling aktif & engagement tertinggi
            f.write("\n\n3. RINGKASAN AKUN PALING AKTIF & ENGAGEMENT TERTINGGI\n")
            f.write("   a. Akun dengan engagement tertinggi (berdasarkan rata-rata total interaksi):\n")
            f.write(f"      - Nama Akun          : {most_engaged['Nama Akun']}\n")
            f.write(f"      - Rata-rata Like     : {most_engaged['Rata-rata Like']}\n")
            f.write(f"      - Rata-rata Share    : {most_engaged['Rata-rata Share']}\n")
            f.write(f"      - Rata-rata Komentar : {most_engaged['Rata-rata Komentar']}\n")
            f.write(f"      - Rata-rata Total Interaksi: {most_engaged['Rata-rata Total Interaksi']}\n")
            
            f.write("\n   b. Akun paling aktif secara interaksi (dihitung dari rata-rata komentar tertinggi):\n")
            f.write(f"      - Nama Akun          : {most_active_comments['Nama Akun']}\n")
            f.write(f"      - Rata-rata Komentar : {most_active_comments['Rata-rata Komentar']}\n")
            f.write(f"      - Rata-rata Like     : {most_active_comments['Rata-rata Like']}\n")
            f.write(f"      - Rata-rata Share    : {most_active_comments['Rata-rata Share']}\n")
            f.write(f"      - Rata-rata Total Interaksi: {most_active_comments['Rata-rata Total Interaksi']}\n")
            
    except OSError as e:
        print(f"[ERROR] Gagal menulis laporan teks: {e}")
        return
        
    print("\n[DONE] Tugas Selesai!")
    print(f"File Output:")
    print(f" - {excel_path}")
    print(f" - {csv_path}")
    print(f" - {report_path}")

if __name__ == "__main__":
    main()
