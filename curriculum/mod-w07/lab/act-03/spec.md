---
activity_id: mod-w07.lab.act-03
component: mod-w07.lab
content_version: "1.0"
variants: [mod-w07.lab.act-03.vA, mod-w07.lab.act-03.vB]
competencies: [comp-w07-algo-01, comp-w07-test-01]
max_points: 30
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W7 · Aktivitas 3 — Algoritma dan Pengujian

## Tujuan

Menelusuri langkah, menemukan langkah ambigu, memilih kasus uji yang mengungkap kesalahan, membedakan hasil yang diharapkan dari hasil langkah yang salah, dan memilih kasus uji batas.

## Prasyarat

Pelajaran 4.

## Asumsi (model modul)

Kasus uji = masukan + hasil yang diharapkan. Langkah dijalankan **persis** seperti tertulis, termasuk bila salah. Bilangan menurut NB-5 (tanda minus untuk bilangan negatif).

**Contoh terlihat (0 poin): kasus uji = masukan + hasil yang diharapkan, mis. "x = 1, y = 2 → 1" untuk bilangan terkecil**

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | Ikuti: (1) mulai dengan 6; (2) kalikan 4; (3) kurangi 9; (4) bagi 3. Hasil? | Ikuti: (1) mulai dengan 7; (2) tambah 5; (3) bagi 4; (4) kalikan 6. Hasil? |
| 02 | Instruksi memasak mi: (1) rebus 400 mL air; (2) masukkan mi; (3) masak **sampai matang**; (4) tiriskan. Langkah mana yang ambigu? (a) Langkah 1, (b) Langkah 2, (c) Langkah 3, (d) Langkah 4 | Instruksi mencetak: (1) buka berkas tugas.pdf; (2) pilih Cetak; (3) atur **jumlah salinan secukupnya**; (4) tekan OK. Langkah mana yang ambigu? (a) Langkah 3, (b) Langkah 1, (c) Langkah 2, (d) Langkah 4 |
| 03 | Langkah "bilangan **terkecil** dari x dan y": (1) jika x < y, hasil = x; (2) selain itu, hasil = x. Kasus uji mana yang mengungkap kesalahan? (a) x = 2, y = 5, (b) x = 9, y = 4, (c) x = 1, y = 8, (d) x = 3, y = 3 | Langkah "**selisih** dua bilangan (yang besar dikurangi yang kecil)": (1) hasil = x − y. Kasus uji mana yang mengungkap kesalahan? (a) x = 8, y = 3, (b) x = 5, y = 5, (c) x = 10, y = 1, (d) x = 2, y = 9 |
| 04 | Untuk kasus uji x = 9, y = 4, berapa hasil yang **diharapkan** (benar)? | Untuk kasus uji x = 2, y = 9, berapa hasil yang **diharapkan** (benar)? |
| 05 | Untuk kasus uji x = 9, y = 4, berapa hasil langkah **yang salah** itu? | Untuk kasus uji x = 2, y = 9, berapa hasil langkah **yang salah** itu? |
| 06 | Aturan: tiket anak bila usia **≤ 12**. Himpunan kasus uji yang **paling baik** menguji batas? (a) {5, 6}, (b) {12, 13}, (c) {20, 30}, (d) {13, 13} | Aturan: gratis ongkir bila belanja **≥ Rp100.000**. Himpunan kasus uji yang **paling baik** menguji batas? (a) {150.000, 200.000}, (b) {20.000, 30.000}, (c) {99.999, 100.000}, (d) {100.000, 100.000} |

## Yang diserahkan

Bilangan untuk 1, 4, 5; huruf opsi untuk 2, 3, 6.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c06 | 5 poin per jawaban benar | 6 × 5 = 30 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong, huruf di luar a–d, atau bentuk yang tidak sesuai → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-ALGO, R-TEST.
