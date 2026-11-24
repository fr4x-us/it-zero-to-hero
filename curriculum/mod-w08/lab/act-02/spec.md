---
activity_id: mod-w08.lab.act-02
component: mod-w08.lab
content_version: "1.0"
variants: [mod-w08.lab.act-02.vA, mod-w08.lab.act-02.vB]
competencies: [comp-w08-loop-01, comp-w08-trace-01]
max_points: 40
estimated_minutes: 40
checks_file: checks.yaml
---

# Lab W8 · Aktivitas 2 — Perulangan dan Tabel Penelusuran

## Tujuan

Menyusun tabel penelusuran perulangan, menentukan output, nilai variabel pengendali saat berhenti, banyak pemeriksaan syarat, dan kasus n = 0.

## Prasyarat

Pelajaran 3.

## Asumsi (model modul)

Flowchart ditulis sebagai **tabel blok bernomor** (Pelajaran 2 §2): setiap blok punya bentuk, isi, dan blok berikutnya; keputusan punya cabang Ya dan Tidak. `←` berarti "beri nilai". Jalankan blok persis seperti tertulis. Jawaban bilangan menurut NB-5 (W5). "Putaran" = satu kali melewati B5 dan B6.

**Contoh terlihat (0 poin): perulangan lain "i ← 1; selama i ≤ 2: tulis i; i ← i + 1" menulis 1, 2**

## Data (fixture): flowchart sebagai tabel blok

**Varian A — Jumlah kuadrat** · Domain input: n bilangan bulat ≥ 0 · Input: n = 4 (pertanyaan 1–7), n = 0 (pertanyaan 8)

| Blok | Bentuk | Isi | Berikutnya |
|---|---|---|---|
| B1 | Oval | `Mulai` | B2 |
| B2 | Jajar genjang | `Input n` | B3 |
| B3 | Persegi panjang | `total ← 0; i ← 1` | B4 |
| B4 | Belah ketupat | `i ≤ n?` | Ya → B5; Tidak → B7 |
| B5 | Persegi panjang | `total ← total + i × i` | B6 |
| B6 | Persegi panjang | `i ← i + 1` | B4 |
| B7 | Jajar genjang | `Output total` | B8 |
| B8 | Oval | `Selesai` | — |

**Varian B — Pangkat dua** · Domain input: n bilangan bulat ≥ 0 · Input: n = 4 (pertanyaan 1–7), n = 0 (pertanyaan 8)

| Blok | Bentuk | Isi | Berikutnya |
|---|---|---|---|
| B1 | Oval | `Mulai` | B2 |
| B2 | Jajar genjang | `Input n` | B3 |
| B3 | Persegi panjang | `hasil ← 1; i ← 1` | B4 |
| B4 | Belah ketupat | `i ≤ n?` | Ya → B5; Tidak → B7 |
| B5 | Persegi panjang | `hasil ← hasil × 2` | B6 |
| B6 | Persegi panjang | `i ← i + 1` | B4 |
| B7 | Jajar genjang | `Output hasil` | B8 |
| B8 | Oval | `Selesai` | — |

## Pertanyaan (fixture)

| No. | Varian A | Varian B |
|---|---|---|
| 01 | Nilai **total** setelah B5 pada putaran ke-1? | Nilai **hasil** setelah B5 pada putaran ke-1? |
| 02 | Nilai **total** setelah B5 pada putaran ke-2? | Nilai **hasil** setelah B5 pada putaran ke-2? |
| 03 | Nilai **total** setelah B5 pada putaran ke-3? | Nilai **hasil** setelah B5 pada putaran ke-3? |
| 04 | Nilai **total** setelah B5 pada putaran ke-4? | Nilai **hasil** setelah B5 pada putaran ke-4? |
| 05 | Output untuk n = 4? | Output untuk n = 4? |
| 06 | Nilai **i** saat perulangan berhenti? | Nilai **i** saat perulangan berhenti? |
| 07 | Berapa kali keputusan B4 diperiksa untuk n = 4? | Berapa kali keputusan B4 diperiksa untuk n = 4? |
| 08 | Output untuk n = 0? | Output untuk n = 0? |

## Yang diserahkan

Bilangan untuk 1–8 (7 boleh diikuti kata `kali`).

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c08 | 5 poin per jawaban benar | 8 × 5 = 40 |
| **Maksimum aktivitas** | | **40** |

## Kasus gagal

Kosong atau bentuk yang tidak sesuai NB-5 → 0 untuk pertanyaan itu; pertanyaan lain tetap dinilai.
Gangguan sistem saat evaluasi → `EVALUATION_ERROR`; evaluasi diulang dari
jawaban yang sama tanpa attempt baru dan tanpa skor 0 (D-24 IE-2).

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan pembahasan langkahnya.

## Remedial

Varian lain menurut VA-1–VA-6 (pemakaian paling sedikit → bukan varian
attempt sebelumnya → indeks terkecil); materi remedial R-LOOP, R-TRACE.
