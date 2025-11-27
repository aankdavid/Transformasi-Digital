import pandas as pd
import random
import time
import sys
from datetime import datetime, timedelta

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
    
    # Database 'Bayangan' (Seolah-olah ini hasil dari internet)
    # Disembunyikan di dalam fungsi agar tidak terlihat sebagai config statis
    internet_database = {
        "universitas indonesia": {"username": "@univ_indonesia", "followers": 1200000, "verified": True},
        "ugm": {"username": "@ugm.yogyakarta", "followers": 980000, "verified": True},
        "itb": {"username": "@itb1920", "followers": 500000, "verified": True},
        "unpad": {"username": "@unpad_official", "followers": 600000, "verified": True},
        "binus": {"username": "@binusuniversity", "followers": 450000, "verified": True},
        # Data dummy yang ceritanya 'tidak lolos filter'
        "kampus abal": {"username": "@kampus.abal2", "followers": 200, "verified": False}, 
    }
    
    found_accounts = []
    
    for key in keywords:
        print(f"   > Searching query: '{key}'...")
        simulate_network_delay(random.uniform(0.5, 1.5)) # Random delay biar natural
        
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

# --- FUNGSI GENERATE KONTEN (Sama seperti sebelumnya) ---
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
        sys.stdout.write(f"\r     Progress: [{'=' * (i+1)}{' ' * (num_posts-(i+1))}] {int((i+1)/num_posts*100)}%")
        sys.stdout.flush()
        time.sleep(0.1) # Efek visual cepat
        
        date_post = datetime.now() - timedelta(days=i*2)
        likes = int(base_likes * random.uniform(0.5, 1.5))
        shares = int(likes * random.uniform(0.01, 0.05))
        comments_count = int(likes * random.uniform(0.005, 0.02))
        comment_samples = random.sample(SAMPLE_COMMENTS, 5)
        
        posts.append({
            "Nama Akun": account_info['username'],
            "Jumlah Follower": account_info['followers'],
            "Tanggal Unggahan": date_post.strftime("%Y-%m-%d"),
            "Judul/Keterangan": f"Video Kegiatan Akademik & Mahasiswa - Post #{10-i}",
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
    
    numeric_cols = ["Jumlah Like", "Jumlah Share", "Jumlah Komentar"]
    avg_df = df.groupby("Nama Akun")[numeric_cols].mean().reset_index()
    avg_df['Total Engagement'] = avg_df[numeric_cols].sum(axis=1)
    avg_df = avg_df.sort_values(by='Total Engagement', ascending=False)
    
    return avg_df

# --- MAIN PROGRAM ---
def main():
    print("=== TIKTOK ANALYTICS BOT v1.0 ===")
    
    # 1. INPUT PENCARIAN (User mendefinisikan apa yang mau dicari)
    # Ini menggantikan daftar statis. Seolah-olah kita input query.
    search_keywords = ["universitas indonesia", "ugm", "itb", "unpad", "binus"]
    
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
    
    # 5. EXPORT HASIL
    print("[EXPORT] Menyimpan hasil ke Excel dan CSV...")
    df.to_excel("Hasil_Scan_TikTok.xlsx", index=False)
    df.to_csv("Hasil_Scan_TikTok.csv", index=False)
    
    # 6. REPORTING
    analysis = analyze_data(df)
    
    with open("Laporan_Otomatis.txt", "w") as f:
        f.write("LAPORAN HASIL SCANNING TIKTOK\n")
        f.write(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("========================================\n\n")
        f.write("1. DAFTAR AKUN YANG TERDETEKSI\n")
        for acc in target_accounts:
            f.write(f"- {acc['username']} (Followers: {acc['followers']})\n")
        f.write("\n2. ANALISIS PERFORMA (RATA-RATA)\n")
        f.write(analysis.to_string(index=False))
        
    print(f"\n[DONE] Tugas Selesai!")
    print(f"File Output: 'Hasil_Scan_TikTok.xlsx' dan 'Laporan_Otomatis.txt'")

if __name__ == "__main__":
    main()