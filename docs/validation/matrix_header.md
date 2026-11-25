# IT ZERO → HERO — Matriks Cakupan Kompetensi W1–W8 (D-39)

Status: **dokumentasi** · audit statis butir · bukan verifikasi runtime atau
uji pelajar. Dibuat oleh generator `docs/validation/build_matrix.py` dari
`coverage_data.py` (pembacaan butir oleh penyusun) dan berkas butir nyata.
Kontrak: **D-39 HYBRID COMPETENCY COVERAGE** ({{DECISIONS_LOG_LINK}}).

## 1. Metode

- **Konsep wajib** = `required_concepts` setiap slot concept (6 slot × 8
  modul); generator memastikan daftar sama persis dengan berkas (tidak ada
  konsep yang dihapus atau diubah, D-39 no. 10).
- **Kelas**: *inti* = dinyatakan langsung dalam teks LO slot (`module.yaml`);
  *pendukung* = dibutuhkan LO tetapi tidak disebut langsung. Klasifikasi
  disusun penyusun, belum dikonfirmasi owner.
- **Dinilai** hanya bila pelajar harus menunjukkan konsep itu untuk
  memperoleh poin: setiap opsi pilihan majemuk (CE-S2/TF-2), pasangan kiri
  (CE-S4), item urutan (CE-S3), baris salah + perbaikan (CE-S5), kunci
  pilihan tunggal (CE-S1/TF-1), isian (TF-3, lab), atau pemeriksaan proyek.
  Tidak dihitung: stem, pengecoh pilihan tunggal, baris CE-S5 yang benar,
  umpan balik, pelajaran, remedial, latihan opsional, refleksi tanpa skor.
- **Jalur penilaian**: VA-2 memilih varian per slot dari riwayat pemakaian
  komponen yang sama untuk semua slot → setiap attempt satu komponen memakai
  indeks varian yang sama (A, lalu B, bergiliran); lab RA-1 per komponen.
  Komponen saling bebas (skor terbaik per komponen, D-12); proyek tanpa
  varian (MPV-A). Jalur sah = {A, B} teori × {A, B} concept × {A, B} lab.
- **Bukti QC-13** (R3-01): (a) **cukup** bila satu lokasi wajib menilai
  konsep di semua varian yang dapat dipilih, atau proyek; (b) **juga sah**
  bila bukti deterministik setara mencakup setiap jalur sah — di sini:
  gabungan lokasi dalam **satu** komponen menutup semua indeks varian
  komponen itu (varian berkorelasi menurut VA-2). Konsep yang memakai bukti
  (b): **{{NB}}**. Aturan pemilihan tidak diubah.
- **Remedial**: bukti berlaku untuk setiap indeks varian, jadi setiap
  attempt remedial (VA-2/VA-3, tanpa batas) tetap tercakup.
- Uji metode (dijalankan generator): hanya varian A → GAP; varian A di dua
  komponen → GAP; lab di kedua varian → PASS; varian A + B di dua slot satu
  komponen → PASS dengan bukti (b).

## 2. Ringkasan cakupan (penulis; belum diverifikasi independen)

{{SUMMARY}}

Riwayat: baseline `a644d61` — 15 GAP (W1 1, W2 8, W3 2, W4 3, W6 1) →
dikoreksi putaran 3. Putaran 4 (review `4ddc993`): R3-04 = koreksi bukti
saja; R3-05, R3-06, R3-07 = bukti penolakan opsi tidak cukup, butir
direvisi minimum; R3-03 = isu keselamatan prosedur dikoreksi. GAP saat ini:
**{{GAPS}}**.

Kesetaraan kompetensi inti (R3-02, §6): **{{EQ_PASS}} PASS**, **{{EQ_OPEN}} OPEN**
dari 48 slot.

## 3. Koreksi butir untuk cakupan (D-39, putaran 3–4)

| Modul | Varian | Perubahan | Konsep | Kunci | Versi |
|---|---|---|---|---|---|
| W1 | teori s10 vB | `16 bit = … byte` | 1 byte = 8 bit | 2 | 2.0 |
| W2 | concept s01 vA | L1 `Kernel` | kernel | L1→R3 | 2.0 |
| W2 | teori s02 vB | opsi c (giliran CPU), e (driver) | manajemen proses, perangkat | a, c, e | 2.0 |
| W2 | teori s05 vA | stem + kunci a (belum disimpan hilang) | yang belum disimpan hilang | a | 2.0 |
| W2 | teori s09 vB | opsi b (aplikasi pembuka) | ekstensi memilih aplikasi | b, c, d | 2.0 |
| W2 | teori s17 vB | langkah 4 pulihkan; opsi b/d ditukar | pulihkan | b | 2.0 |
| W2 | concept s05 vA | simulasi; periksa **seluruh** isi Tempat Sampah sebelum mengosongkan (R3-03) | periksa sebelum menghapus permanen | A B C D | 3.0 |
| W2 | concept s05 vB | idem langkah D (R3-03) | idem | A B C D | 2.0 |
| W2 | concept s06 vB | opsi c (akun administrator) | akun biasa vs admin | b, d | 2.0 |
| W3 | concept s02 vB | opsi e: "tidak dapat berbagi satu alamat publik" (R3-05) | NAT berbagi alamat publik | a, c, d | 3.0 |
| W3 | teori s08 vB | host tersisa setelah router | 254 host | 253 | 2.0 |
| W4 | concept s02 vB | opsi a (phishing = RS); opsi e "belum membuktikan" (R3-06) | phishing RS; tanda bukan bukti | b, c, e | 3.0 |
| W4 | concept s04 vA | kunci b memuat arti HTTPS | HTTPS bukan bukti identitas | b | 2.0 |
| W4 | concept s05 vA | stem "pernyataan yang benar"; opsi b satu klaim (R3-07) | perlindungan tidak menjamin | a, c | 3.0 |
| W6 | concept s05 vB | opsi e (urutan baris standar) | urutan baris standar | b, c, e | 2.0 |

Format, poin, kompetensi, dan distribusi posisi kunci setiap modul tidak
berubah (`check_keys.py`, snapshot = baseline `4ddc993`). Varian W1–W4 di
atas **belum diterima** (TPL-01a `acceptance.revised_variants`, PENDING).

## 4. Register temuan reviewer putaran 3 (ID sementara; F-73–F-94 asli tidak tersedia)

| ID | Temuan | Disposisi | AUTHOR RESOLVED | INDEPENDENT VERIFIED |
|---|---|---|---|---|
| R3-01 | Metode bukti QC-13 terlalu sempit | DOCUMENTATION CLARIFIED (QC-13 a/b, TPL-13, §1) | YA | BELUM |
| R3-02 | Kesetaraan 96/96 tanpa register | DOCUMENTATION CLARIFIED (§6, 48 slot; OPEN dilaporkan) | YA | BELUM |
| R3-03 | W2 concept s05: mengosongkan seluruh Tempat Sampah setelah memeriksa satu berkas | CONFIRMED — FIXED (vA, vB; simulasi) | YA | BELUM |
| R3-04 | Bukti "salin mempertahankan asal" pada teori s17 vA tidak sah | CONFIRMED (bukti) — matriks dikoreksi; cakupan dijamin proyek K4.q3 | YA | BELUM |
| R3-05 | NAT: penolakan opsi tidak menuntut konsep berbagi | CONFIRMED — FIXED (W3 concept s02 vB opsi e) | YA | BELUM |
| R3-06 | Tanda vs bukti: vB opsi e tidak menuntut "bukan bukti" | CONFIRMED — FIXED (W4 concept s02 vB opsi e) | YA | BELUM |
| R3-07 | Pernyataan majemuk W4 concept s05 vA opsi b | CONFIRMED — FIXED (tidak ada lokasi wajib lain; opsi dijadikan satu klaim) | YA | BELUM |
| R3-08 | Status penerimaan hanya di komentar YAML | CONFIRMED — FIXED (TPL-01a `acceptance`, `check_acceptance.py`) | YA | BELUM |
| PR28-06 | Cakupan `required_concepts` | D-39 dicatat; audit dan koreksi penulis | YA | BELUM |
| PR28-02 | NB-5 | Paket reproduksi `docs/validation/` | YA | BELUM (PARTIAL PASS independen) |
