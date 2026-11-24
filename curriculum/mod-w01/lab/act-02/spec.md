---
activity_id: mod-w01.lab.act-02
component: mod-w01.lab
content_version: "1.0"
variants: [mod-w01.lab.act-02.vA, mod-w01.lab.act-02.vB]
competencies: [comp-w01-ipos-01, comp-w01-sw-01]
max_points: 30
estimated_minutes: 30
checks_file: checks.yaml
---

# Lab W1 · Aktivitas 2 — Alur IPOS dan Lapisan Software

## Tujuan

1. Mengurutkan kejadian nyata sesuai alur kerja komputer.
2. Menandai tahap IPOS setiap kejadian.
3. Menentukan software yang menghubungkan sistem operasi dengan perangkat.

## Prasyarat

Pelajaran 1 dan Pelajaran 3.

## Instruksi

1. Baca empat kejadian (ditampilkan acak).
2. **Bagian 1 —** susun keempat kejadian sesuai urutan terjadinya.
3. **Bagian 2 —** beri label tahap untuk setiap kejadian: `I` Input, `P`
   Proses, `O` Output, `S` Penyimpanan.
4. **Bagian 3 —** jawab pertanyaan lapisan software.
5. Tekan **Serahkan**.

**Contoh terlihat (tidak dinilai):** "Menekan tombol volume" → Input.

## Data (fixture)

**Varian A — memesan tiket kereta** (ditampilkan urutan C, A, D, B)

| ID | Kejadian |
|---|---|
| A | Kamu mengetik kota tujuan dan tanggal di aplikasi tiket kereta |
| B | Aplikasi mencari jadwal kereta yang cocok |
| C | Daftar jadwal tampil di layar |
| D | Setelah memilih jadwal di layar, tiket disimpan di penyimpanan ponsel |

Pertanyaan lapisan: *Software apa yang membantu sistem operasi ponsel membaca
sentuhan jarimu pada layar?* (a) aplikasi tiket kereta, (b) firmware
pengisi daya, (c) baterai, (d) driver layar sentuh.

**Varian B — memotret** (ditampilkan urutan B, D, A, C)

| ID | Kejadian |
|---|---|
| A | Sensor kamera ponsel menangkap gambar |
| B | Prosesor ponsel memperbaiki kecerahan foto |
| C | Foto tampil di layar untuk kamu periksa |
| D | Setelah puas, kamu menyimpan foto ke penyimpanan internal |

Pertanyaan lapisan: *Software apa yang membantu sistem operasi ponsel memakai
sensor kamera?* (a) aplikasi galeri, (b) baterai, (c) driver kamera,
(d) firmware pengisi daya.

## Yang diserahkan

Urutan empat ID, empat label tahap, satu pilihan lapisan.

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01 Urutan | 3 poin per pasangan berurutan yang benar terhadap urutan diterima A → B → C → D (maks. 3 pasangan) | 12 |
| c02–c05 Label tahap | 3 poin per label benar | 12 |
| c06 Lapisan software | Pilihan tunggal | 6 |
| **Maksimum aktivitas** | | **30** |

Contoh hitung urutan: jawaban `A, B, D, C` → pasangan A→B benar, B→D salah,
D→C salah → 1 pasangan → 3 poin. Jawaban `A, B, C, D` → 3 pasangan → 12
poin. Urutan yang memuat ID ganda atau tidak dikenal → 0 poin untuk c01.

## Kasus gagal

Kosong → 0 untuk pemeriksaan itu; ID tidak dikenal/ganda → 0 untuk
pemeriksaan itu; gangguan sistem → evaluasi diulang tanpa attempt baru.

## Umpan balik

Urutan yang benar, label setiap kejadian, dan alasan: driver adalah software
penghubung sistem operasi dengan perangkat tertentu.

## Remedial

Varian lain menurut VA-2; ulangi Pelajaran 1 §3–§5 dan Pelajaran 3 §2;
materi remedial R-IPOS dan R-SW.
