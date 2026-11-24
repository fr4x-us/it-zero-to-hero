---
module_id: mod-w08
content_version: "1.0"
template: TPL-14
purpose: "Penjelasan ulang dan latihan tambahan per kompetensi untuk persiapan remedial (tidak dinilai)"
---

# Materi Remedial W8

Gunakan bagian yang sesuai dengan kompetensi yang belum dikuasai (umpan
balik ujian menampilkan rincian per kompetensi, FB-A). Latihan di sini tidak
dinilai dan tidak memberi XP. Attempt remedial memakai **varian setara**
yang dipilih menurut VA-1–VA-6: varian dengan pemakaian paling sedikit,
bila seri bukan varian attempt sebelumnya, bila masih seri indeks terkecil
(VA-2; pemakaian ulang VA-3); remedial tidak dibatasi jumlahnya. Contoh di
sini berbeda dari soal bernilai.

## R-ALGO — Algoritma dan domain (LO1)

**Ingat kembali:** input → proses → output; berhenti; `←` memberi nilai;
domain = input yang boleh diberikan.

**Latihan tambahan:** `harga_satuan ← total ÷ jumlah_barang`. Tulis
domain `jumlah_barang`. *Jawaban:* bilangan bulat ≥ 1 (tidak boleh 0).

## R-SYMBOL — Simbol flowchart (LO2)

**Ingat kembali:** oval mulai/selesai; jajar genjang input/output; persegi
panjang proses; belah ketupat keputusan dengan dua cabang.

**Latihan tambahan:** bentuk untuk `Input umur`? untuk `umur ≥ 17?`?
*Jawaban:* jajar genjang; belah ketupat.

## R-BRANCH — Percabangan (LO3)

**Ingat kembali:** periksa berurutan, berhenti di cabang pertama yang
cocok; `≥` termasuk sama dengan.

**Latihan tambahan:** jika `jarak ≥ 10` → "jauh"; selain itu jika
`jarak ≥ 3` → "sedang"; selain itu "dekat". Output untuk jarak 10, 3, 2?
*Jawaban:* "jauh", "sedang", "dekat".

## R-LOOP — Perulangan (LO4)

**Ingat kembali:** nilai awal sekali; syarat diperiksa putaran + 1 kali;
perubahan harus mendekatkan ke berhenti.

**Latihan tambahan:** `p ← 3`; selama `p ≤ 7`: `p ← p + 2`. Berapa
putaran, berapa pemeriksaan, nilai p akhir? *Jawaban:* p = 3, 5, 7 → 3
putaran; 4 pemeriksaan; p = 9.

## R-TRACE — Tabel penelusuran (LO5)

**Ingat kembali:** kolom per variabel; nilai lama berlaku sampai diganti.

**Latihan tambahan:** `x ← 2`; `y ← x + 4`; `x ← y − x`; `y ← x × 2`.
*Jawaban:* x 2, y 6, x 4, y 8.

## R-CORRECT — Kebenaran algoritma (LO6)

**Ingat kembali:** nilai awal 0 untuk jumlah, 1 untuk perkalian, nilai
pertama daftar untuk pembanding; uji satu nilai, semua negatif, nilai sama,
nilai penting di akhir.

**Latihan tambahan:** algoritma **jumlah** daftar memakai `total ← 1`.
Kasus uji mana yang mengungkapnya: `[0]` atau tidak ada? *Jawaban:* `[0]`
memberi 1 padahal jumlahnya 0 (sebenarnya setiap daftar mengungkapnya:
hasil selalu lebih 1).
