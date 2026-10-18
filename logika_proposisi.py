# ==============================================================================
# PROGRAM UTAMA: KALKULATOR TABEL KEBENARAN LOGIKA PROPOSISI (PROSEDURAL)
# ==============================================================================

def cetak_header():
    """Menampilkan judul dan informasi program."""
    print("=" * 60)
    print("      PROGRAM EVALUATOR LOGIKA PROPOSISI & TABEL KEBENARAN      ")
    print("==============================================================")
    print("Keterangan Operasi Logika:")
    print(" 1. NOT (Negasi)       : ~P")
    print(" 2. AND (Konjungsi)    : P AND Q")
    print(" 3. OR  (Disjungsi)    : P OR Q")
    print(" 4. IMPLIKASI          : P -> Q  (Jika P maka Q)")
    print(" 5. BIIMPLIKASI        : P <-> Q (P jika dan hanya jika Q)")
    print("=" * 60)


def logika_not(p):
    """Menghitung negasi (~P)."""
    return not p


def logika_and(p, q):
    """Menghitung konjungsi (P AND Q)."""
    return p and q


def logika_or(p, q):
    """Menghitung disjungsi (P OR Q)."""
    return p or q


def logika_implikasi(p, q):
    """Menghitung implikasi (P -> Q).
    Implikasi bernilai False HANYA JIKA P = True dan Q = False.
    """
    return (not p) or q


def logika_biimplikasi(p, q):
    """Menghitung biimplikasi (P <-> Q).
    Biimplikasi bernilai True JIKA nilai kebenaran P dan Q SAMA.
    """
    return p == q


def format_boolean(nilai):
    """Mengubah nilai boolean True/False menjadi karakter T/F untuk konsistensi."""
    return "T" if nilai else "F"


def buat_tabel_kebenaran_lengkap():
    """Menghasilkan dan menampilkan tabel kebenaran lengkap untuk P dan Q
    terhadap seluruh operasi logika dasar.
    """
    print("\n[ TABEL KEBENARAN LOGIKA DASAR ]\n")
    # Header Tabel
    print(f"|  P  |  Q  | ~P  | P AND Q | P OR Q | P -> Q | P <-> Q |")
    print("-" * 57)

    # Kombinasi nilai kebenaran untuk 2 variabel (True/False)
    kombinasi_p_q = [(True, True), (True, False), (False, True), (False, False)]

    for p, q in kombinasi_p_q:
        not_p = logika_not(p)
        and_op = logika_and(p, q)
        or_op = logika_or(p, q)
        impl_op = logika_implikasi(p, q)
        biimpl_op = logika_biimplikasi(p, q)

        # Format setiap baris output
        p_str = format_boolean(p)
        q_str = format_boolean(q)
        not_p_str = format_boolean(not_p)
        and_str = format_boolean(and_op)
        or_str = format_boolean(or_op)
        impl_str = format_boolean(impl_op)
        biimpl_str = format_boolean(biimpl_op)

        print(
            f"|  {p_str}  |  {q_str}  |  {not_p_str}  |    {and_str}    |   {or_str}    |   {impl_str}    |    {biimpl_str}    |"
        )

    print("-" * 57)


def evaluasi_ekspresi_kustom(p, q):
    """Mengevaluasi bentuk proposisi majemuk khusus: ((P -> Q) AND P) -> Q
    (Bentuk argumen valid: Modus Ponens).
    """
    p_impl_q = logika_implikasi(p, q)
    hipotesis = logika_and(p_impl_q, p)
    hasil_akhir = logika_implikasi(hipotesis, q)
    return p_impl_q, hipotesis, hasil_akhir


def buat_tabel_modus_ponens():
    """Menampilkan pembuktian Tautologi Modus Ponens: ((P -> Q) AND P) -> Q."""
    print("\n[ PEMBUKTIAN TAUTOLOGI: MODUS PONENS ]")
    print("Formula: ((P -> Q) AND P) -> Q\n")
    print(f"|  P  |  Q  | P -> Q | (P->Q) AND P | Hasil Akhir |")
    print("-" * 53)

    kombinasi_p_q = [(True, True), (True, False), (False, True), (False, False)]

    semua_true = True
    for p, q in kombinasi_p_q:
        p_impl_q, hipotesis, hasil = evaluasi_ekspresi_kustom(p, q)

        if not hasil:
            semua_true = False

        print(
            f"|  {format_boolean(p)}  |  {format_boolean(q)}  |   {format_boolean(p_impl_q)}    |      {format_boolean(hipotesis)}       |      {format_boolean(hasil)}      |"
        )

    print("-" * 53)
    if semua_true:
        print("Kesimpulan: Ekspresi tersebut adalah TAUTOLOGI (Selalu bernilai True).")
    else:
        print("Kesimpulan: Ekspresi tersebut BUKAN Tautologi.")


def jalankan_program():
    """Fungsi utama pengendali alur eksekusi prosedural."""
    cetak_header()
    buat_tabel_kebenaran_lengkap()
    buat_tabel_modus_ponens()
    print("\nProgram selesai dieksekusi.")


# ==============================================================================
# TITIK MASUK PROGRAM (ENTRY POINT)
# ==============================================================================
if __name__ == "__main__":
    jalankan_program()
