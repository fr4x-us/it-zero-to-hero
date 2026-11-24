---
activity_id: mod-w02.lab.act-02
component: mod-w02.lab
content_version: "1.0"
variants: [mod-w02.lab.act-02.vA, mod-w02.lab.act-02.vB]
competencies: [comp-w02-path-01]
max_points: 30
estimated_minutes: 30
checks_file: checks.yaml
---

# Lab W2 · Aktivitas 2 — Path Absolut dan Relatif

## Tujuan

1. Menulis path absolut berkas dan folder dari pohon folder.
2. Menulis path relatif **terpendek** dari folder kerja tertentu, termasuk
   memakai `..`.

## Prasyarat

Pelajaran 3 §3–§6.

## Aturan jawaban (model path W2)

- Pemisah `/`; huruf besar/kecil **dibedakan**; tanpa spasi; path ke
  folder tidak diakhiri `/`.
- Path relatif boleh ditulis dengan atau tanpa awalan `./`.
- Path relatif harus **terpendek** (tanpa naik-turun yang tidak perlu).

**Contoh terlihat (tidak dinilai, pohon lain):** dari folder kerja
`/contoh/a` ke berkas `/contoh/b/c.txt` → `../b/c.txt`.

## Data (fixture)

**Varian A**

```
/
└── home
    └── nadia
        ├── Sekolah
        │   ├── Kimia
        │   │   └── laporan-kimia.docx
        │   └── jadwal-ujian.pdf
        ├── Gambar
        │   └── Kucing
        │       └── milo.jpg
        └── Musik
            └── angklung.mp3
```

*Deskripsi pohon A:* root → `home` → `nadia`. `nadia` berisi `Sekolah`,
`Gambar`, `Musik`. `Sekolah` berisi folder `Kimia` (berisi
`laporan-kimia.docx`) dan berkas `jadwal-ujian.pdf`. `Gambar` berisi folder
`Kucing` (berisi `milo.jpg`). `Musik` berisi `angklung.mp3`.

| No. | Pertanyaan |
|---|---|
| 1 | Path absolut berkas `laporan-kimia.docx` |
| 2 | Path absolut folder `Kucing` |
| 3 | Path absolut berkas `angklung.mp3` |
| 4 | Folder kerja `/home/nadia/Sekolah` → path relatif ke `laporan-kimia.docx` |
| 5 | Folder kerja `/home/nadia/Sekolah/Kimia` → path relatif ke `jadwal-ujian.pdf` |
| 6 | Folder kerja `/home/nadia/Sekolah/Kimia` → path relatif ke `milo.jpg` |

**Varian B**

```
/
└── home
    └── yusuf
        ├── Kerja
        │   ├── Proposal
        │   │   └── proposal-akhir.docx
        │   └── kontak-klien.csv
        ├── Video
        │   └── Liburan
        │       └── danau.mp4
        └── Buku
            └── novel-ringkas.pdf
```

*Deskripsi pohon B:* root → `home` → `yusuf`. `yusuf` berisi `Kerja`,
`Video`, `Buku`. `Kerja` berisi folder `Proposal` (berisi
`proposal-akhir.docx`) dan berkas `kontak-klien.csv`. `Video` berisi folder
`Liburan` (berisi `danau.mp4`). `Buku` berisi `novel-ringkas.pdf`.

| No. | Pertanyaan |
|---|---|
| 1 | Path absolut berkas `proposal-akhir.docx` |
| 2 | Path absolut folder `Liburan` |
| 3 | Path absolut berkas `novel-ringkas.pdf` |
| 4 | Folder kerja `/home/yusuf/Kerja` → path relatif ke `proposal-akhir.docx` |
| 5 | Folder kerja `/home/yusuf/Kerja/Proposal` → path relatif ke `kontak-klien.csv` |
| 6 | Folder kerja `/home/yusuf/Kerja/Proposal` → path relatif ke `danau.mp4` |

## Yang diserahkan

Enam path (teks).

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c03 | Path absolut cocok persis | 3 × 5 = 15 |
| c04–c06 | Path relatif terpendek cocok persis (dengan/tanpa `./`) | 3 × 5 = 15 |
| **Maksimum aktivitas** | | **30** |

## Kasus gagal

Kosong; memakai `\`; spasi di dalam path; huruf besar/kecil berbeda; `/`
di akhir; path relatif yang memutar → 0 untuk pemeriksaan itu. Pemeriksaan
lain tetap dinilai. Gangguan sistem → evaluasi diulang tanpa attempt baru.

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan path yang benar untuk varian yang kamu
kerjakan.

## Remedial

Varian lain menurut VA-2; ulangi Pelajaran 3 §4–§6; materi remedial
R-PATH.
