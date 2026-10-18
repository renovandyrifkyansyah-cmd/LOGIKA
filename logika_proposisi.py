import os
import time

# ==============================================================================
# STRUKTUR DATA SOAL KUIS (Kuis Berbasis Skenario Kehidupan Nyata)
# ==============================================================================
DAFTAR_SOAL = [
    {
        "kategori": "Implikasi (Jika P Maka Q)",
        "cerita": "Janji Ibu: 'Jika kamu dapat nilai A pada ujian Matematika, maka Ibu akan belikan Sepatu Baru.'",
        "pertanyaan": "Kapan janji Ibu dianggap DIINGKARI (Bernilai SALAH/False)?",
        "pilihan": [
            "A. Kamu dapat nilai A, dan Ibu belikan Sepatu Baru.",
            "B. Kamu dapat nilai A, tetapi Ibu TIDAK membelikan Sepatu Baru.",
            "C. Kamu TIDAK dapat nilai A, tetapi Ibu tetap membelikan Sepatu Baru.",
            "D. Kamu TIDAK dapat nilai A, dan Ibu TIDAK membelikan Sepatu Baru."
        ],
        "kunci": "B",
        "penjelasan": "Implikasi (P -> Q) hanya bernilai SALAH jika sebabnya terjadi (P = True), tetapi akibatnya tidak ditepati (Q = False)."
    },
    {
        "kategori": "Negasi / Ingkaran",
        "cerita": "Pernyataan: 'Semua siswa kelas 12 lulus ujian nasional.'",
        "pertanyaan": "Apa ingkaran (negasi) yang paling tepat dari pernyataan di atas?",
        "pilihan": [
            "A. Semua siswa kelas 12 tidak lulus ujian nasional.",
            "B. Tidak ada siswa kelas 12 yang lulus ujian nasional.",
            "C. Ada setidaknya satu siswa kelas 12 yang tidak lulus ujian nasional.",
            "D. Beberapa siswa kelas 12 lulus ujian nasional."
        ],
        "kunci": "C",
        "penjelasan": "Ingkaran dari Kuantor Universal ('Semua P') adalah Kuantor Eksistensial ('Ada/Beberapa P yang Bukan'). Cukup 1 orang gagal untuk membantah kata 'Semua'."
    },
    {
        "kategori": "Penarikan Kesimpulan (Modus Ponens)",
        "cerita": "Premis 1: Jika hari hujan, maka lapangan sekolah becek.\nPremis 2: Hari ini hujan deras.",
        "pertanyaan": "Kesimpulan yang sah (valid) adalah...",
        "pilihan": [
            "A. Lapangan sekolah becek.",
            "B. Lapangan sekolah tidak becek.",
            "C. Hari ini tidak hujan.",
            "D. Lapangan sekolah digunakan untuk main bola."
        ],
        "kunci": "A",
        "penjelasan": "Mengikuti aturan Modus Ponens: [(P -> Q) DAN P] menyimpulkan Q."
    }
]

# ==============================================================================
# FUNGSI PENDUKUNG MEDIA AJAR
# ==============================================================================

def bersihkan_layar():
    """Layar dibersihkan agar tampilan terminal rapi ala aplikasi modern."""
    os.system('cls' if os.name == 'nt' else 'clear')


def cetak_header(judul):
    """Mencetak header visual yang menarik."""
    print("=" * 65)
    print(f"   {judul.upper()}")
    print("=" * 65)


def tampilkan_papan_skor(skor, total_soal):
    """Menampilkan ringkasan hasil belajar siswa."""
    bersihkan_layar()
    cetak_header("Hasil Akhir Kuis Logika Matematika")
    
    persentase = (skor / total_soal) * 100
    print(f"\nSkor Kamu : {skor} dari {total_soal} soal ({persentase:.0f}%)\n")
    
    if persentase == 100:
        print("Peringkat: MASTER LOGIKA!")
        print("Pikiranmu sangat tajam, tidak mudah terkecoh oleh janji manis maupun argumen sesat!")
    elif persentase >= 60:
        print("Peringkat: DETEKTIF LOGIKA!")
        print("Kemampuan logikamu sudah bagus, tinggal sedikit melatih ketelitian.")
    else:
        print("Peringkat: PEMULA LOGIKA!")
        print("Jangan berkecil hati! Logika adalah melatih pola pikir, ayo coba lagi!")
        
    print("\n" + "=" * 65)


# ==============================================================================
# MODUL UTAMA APLIKASI
# ==============================================================================

def modul_simulator_tabel():
    """Fitur eksplorasi tabel kebenaran interaktif."""
    bersihkan_layar()
    cetak_header("Simulator Tabel Kebenaran Interaktif")
    
    print("\nPilih dua nilai kebenaran untuk uji coba:")
    print("Pernyataan P (misal: 'Hari Hujan')")
    p_input = input("Apakah P Benar? (y/n): ").strip().lower() == 'y'
    
    print("\nPernyataan Q (misal: 'Lapangan Becek')")
    q_input = input("Apakah Q Benar? (y/n): ").strip().lower() == 'y'
    
    p_str = "BENAR (T)" if p_input else "SALAH (F)"
    q_str = "BENAR (T)" if q_input else "SALAH (F)"
    
    bersihkan_layar()
    cetak_header("Hasil Evaluasi Logika")
    print(f"\nStatus Input : P = {p_str} | Q = {q_str}\n")
    
    print(f"1. Negasi (~P)        : {'SALAH (F)' if p_input else 'BENAR (T)'}")
    print(f"2. Konjungsi (P AND Q): {'BENAR (T)' if (p_input and q_input) else 'SALAH (F)'}")
    print(f"3. Disjungsi (P OR Q) : {'BENAR (T)' if (p_input or q_input) else 'SALAH (F)'}")
    
    # Implikasi
    implikasi = (not p_input) or q_input
    print(f"4. Implikasi (P -> Q) : {'BENAR (T)' if implikasi else 'SALAH (F)'}")
    
    # Biimplikasi
    biimplikasi = p_input == q_input
    print(f"5. Biimplikasi (P<->Q): {'BENAR (T)' if biimplikasi else 'SALAH (F)'}")
    
    print("\n" + "=" * 65)
    input("\nTekan Enter untuk kembali ke menu utama...")


def modul_kuis_interaktif():
    """Fitur kuis berbasis cerita untuk siswa SMA."""
    skor = 0
    total = len(DAFTAR_SOAL)
    
    for idx, soal in enumerate(DAFTAR_SOAL, start=1):
        bersihkan_layar()
        cetak_header(f"Soal {idx}/{total} - {soal['kategori']}")
        
        print(f"\n[Skenario]:\n{soal['cerita']}\n")
        print(f"[Pertanyaan]:\n{soal['pertanyaan']}\n")
        
        for pil in soal["pilihan"]:
            print(f"  {pil}")
            
        jawab = input("\nJawaban Kamu (A/B/C/D): ").strip().upper()
        
        if jawab == soal["kunci"]:
            print("\n  JAWABAN BENAR! Bagus sekali!")
            skor += 1
        else:
            print(f"\n  JAWABAN KURANG TEPAT. Jawaban yang benar adalah {soal['kunci']}.")
            
        print(f"\n[Penjelasan Logika]:\n{soal['penjelasan']}")
        print("\n" + "-" * 65)
        input("Tekan Enter untuk melanjutkan ke soal berikutnya...")
        
    tampilkan_papan_skor(skor, total)
    input("\nTekan Enter untuk kembali ke menu utama...")


def menu_utama():
    """Menu navigasi utama media ajar."""
    while True:
        bersihkan_layar()
        cetak_header("MEDIA AJAR INTERAKTIF: LOGIKA MATEMATIKA SMA")
        print("\nSelamat Datang! Silahkan pilih modul belajar:\n")
        print("  [1] Kuis Logika Skenario Kehidupan Nyata")
        print("  [2] Simulator Tabel Kebenaran Interaktif")
        print("  [3] Keluar dari Aplikasi")
        print("\n" + "=" * 65)
        
        pilihan = input("\nPilih Menu (1/2/3): ").strip()
        
        if pilihan == '1':
            modul_kuis_interaktif()
        elif pilihan == '2':
            modul_simulator_tabel()
        elif pilihan == '3':
            bersihkan_layar()
            print("Terima kasih telah belajar Logika Matematika! Sampai jumpa!")
            break


# ==============================================================================
# TITIK MASUK APLIKASI
# ==============================================================================
if __name__ == "__main__":
    menu_utama()
