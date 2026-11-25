---
module_id: mod-w06
content_version: "1.0"
template: TPL-14
purpose: "Penjelasan ulang dan latihan tambahan per kompetensi untuk persiapan remedial (tidak dinilai)"
---

# Materi Remedial W6

Gunakan bagian yang sesuai dengan kompetensi yang belum dikuasai (umpan
balik ujian menampilkan rincian per kompetensi, FB-A). Latihan di sini tidak
dinilai dan tidak memberi XP. Attempt remedial memakai **varian setara**
yang dipilih menurut VA-1–VA-6: varian dengan pemakaian paling sedikit,
bila seri bukan varian attempt sebelumnya, bila masih seri indeks terkecil
(VA-2; pemakaian ulang VA-3); remedial tidak dibatasi jumlahnya. Angka dan
ekspresi di sini berbeda dari soal bernilai.

## R-REPR — Bit, basis, dan jenis nilai (LO1)

**Ingat kembali:** bit = 0 atau 1; posisi dari kanan mulai 0; bobot =
2^posisi; `x₂` biner, `x₁₀` desimal; Boolean 1/0 = benar/salah.

**Latihan tambahan:** (1) bobot posisi 4? (2) `100₂` dan `100₁₀` —
masing-masing bernilai/dibaca apa? *Jawaban:* (1) 16; (2) `100₂` = 4,
`100₁₀` = seratus.

## R-BIN2DEC — Biner ke desimal (LO2)

**Ingat kembali:** jumlahkan bobot bit 1; nol di depan tidak menambah nilai.

**Latihan tambahan:** (1) `100111₂`; (2) `01011000₂`. *Jawaban:*
(1) 32 + 4 + 2 + 1 = 39; (2) 64 + 16 + 8 = 88.

## R-DEC2BIN — Desimal ke biner (LO3)

**Ingat kembali:** kurangi bobot terbesar, atau bagi 2 berulang dan baca
sisa dari bawah; nol hanya di depan; n bit: 0 sampai 2ⁿ − 1.

**Latihan tambahan:** (1) 41 tanpa nol di depan; (2) 7 tepat 8 bit;
(3) nilai terbesar 10 bit. *Jawaban:* (1) `101001`; (2) `00000111`;
(3) 1.023.

## R-OPS — AND, OR, NOT (LO4)

**Ingat kembali:** AND semua 1; OR sedikitnya satu 1 (keduanya 1 juga 1);
NOT membalik.

**Latihan tambahan:** X = 1, Y = 0: (1) `X OR Y`; (2) `NOT X AND Y`.
*Jawaban:* (1) 1; (2) 0.

## R-TABLE — Tabel kebenaran (LO5)

**Ingat kembali:** 2ⁿ baris; urutan seperti menghitung biner; prioritas
kurung → NOT → AND → OR; kolom bantu.

**Latihan tambahan:** berapa baris bernilai 1 pada `X AND Y AND Z`? Dan
pada `X OR Y OR Z`? *Jawaban:* 1 baris; 7 baris.

## R-MODEL — Memodelkan aturan (LO6)

**Ingat kembali:** tentukan variabel → terjemahkan → kurung → periksa
semua baris; ekspresi ekuivalen sama-sama benar.

**Latihan tambahan:** "Bel istirahat berbunyi bila jam menunjukkan 10.00
(J) dan hari ini bukan hari libur (L)." *Jawaban:* `J AND NOT L`
(atau `NOT L AND J`).
