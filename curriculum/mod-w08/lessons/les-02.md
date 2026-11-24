---
lesson_id: mod-w08.les-02
practice_id: mod-w08.prac-02
module_id: mod-w08
content_version: "1.0"
title: "Simbol Flowchart dan Percabangan"
language: id
duration_minutes: 35        # materi 25 + latihan terbimbing 10
competencies: [comp-w08-symbol-01, comp-w08-branch-01]
prerequisites: [mod-w08.les-01]
accessibility:
  diagrams:
    - id: dg-w08-02
      alt: "Empat bentuk flowchart."
      long_description: >
        Oval berlabel Mulai/Selesai; jajar genjang berlabel Input/Output;
        persegi panjang berlabel Proses; belah ketupat berlabel Keputusan
        dengan dua panah keluar Ya dan Tidak.
    - id: dg-w08-02b
      alt: "Flowchart diskon belanja sebagai tabel blok."
      long_description: >
        Tujuh blok: Mulai, Input total, keputusan total ≥ 200000 dengan
        cabang Ya ke bayar ← total − 20000 dan cabang Tidak ke bayar ←
        total, keduanya menuju Output bayar, lalu Selesai.
  tables_with_core_data: ["Tabel simbol", "Tabel blok contoh", "Tabel percabangan bertingkat"]
  english_terms: [flowchart, terminator, input/output, process, decision, arrow, branch, nested decision, boundary]
---

# Pelajaran 2 — Simbol Flowchart dan Percabangan

## Tujuan pelajaran

Setelah pelajaran ini kamu dapat:

1. Mengenali simbol flowchart.
2. Membaca flowchart yang ditulis sebagai **tabel blok**.
3. Menelusuri **percabangan** tunggal dan **bertingkat**, termasuk nilai
   tepat di batas.

## Mengapa ini penting?

Flowchart membuat urutan dan pilihan langkah terlihat. Dua orang yang
membaca flowchart yang sama akan menjalankan langkah yang sama — syarat
utama algoritma.

## 1. Simbol

*Deskripsi diagram dg-w08-02:* oval, jajar genjang, persegi panjang, belah
ketupat.

| Bentuk | Kegunaan | Contoh isi |
|---|---|---|
| Oval | Mulai / Selesai | Mulai |
| Jajar genjang | Input / Output | Input nilai |
| Persegi panjang | Proses | `luas ← p × l` |
| Belah ketupat | Keputusan Ya/Tidak | `nilai ≥ 75?` |
| Panah | Arah langkah berikutnya | |

## 2. Flowchart sebagai tabel blok

Di W8, flowchart ditulis sebagai tabel: setiap **blok** punya nomor,
bentuk, isi, dan blok berikutnya. Keputusan punya dua tujuan: **Ya** dan
**Tidak**. Bentuk tabel ini setara dengan gambar flowchart — banyak gambar
berbeda dapat menyatakan tabel yang sama.

*Deskripsi diagram dg-w08-02b:* flowchart diskon.

| Blok | Bentuk | Isi | Berikutnya |
|---|---|---|---|
| B1 | Oval | Mulai | B2 |
| B2 | Jajar genjang | Input total | B3 |
| B3 | Belah ketupat | `total ≥ 200000?` | Ya → B4; Tidak → B5 |
| B4 | Persegi panjang | `bayar ← total − 20000` | B6 |
| B5 | Persegi panjang | `bayar ← total` | B6 |
| B6 | Jajar genjang | Output bayar | B7 |
| B7 | Oval | Selesai | — |

Telusuri **total = 200000**: B3 → `200000 ≥ 200000` **benar** (≥ termasuk
sama dengan) → B4 → bayar = 180000.

## 3. Percabangan bertingkat

Keputusan dapat diikuti keputusan lain. Periksa **berurutan**; berhenti di
cabang pertama yang cocok.

| Urutan | Pemeriksaan |
|---|---|
| 1 | Jika `poin ≥ 1000` → "emas" |
| 2 | Selain itu, jika `poin ≥ 500` → "perak" |
| 3 | Selain itu → "perunggu" |

poin = 500: pemeriksaan 1 salah; pemeriksaan 2 benar → "perak".
poin = 499: 1 salah, 2 salah → "perunggu".

**Uji batas** (W7): uji tepat di batas (500) dan di sebelahnya (499).

## 4. Contoh terbimbing

**Soal:** Untuk tabel blok diskon di atas, blok apa saja yang dilewati
untuk total = 150000, dan berapa output?

1. B1 → B2 → B3: `150000 ≥ 200000` salah → B5.
2. B5: bayar = 150000 → B6 → B7.
3. Jalur: B1 B2 B3 B5 B6 B7; output 150000.

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Keputusan boleh punya satu panah keluar" | Selalu dua: Ya dan Tidak |
| "≥ sama dengan >" | ≥ termasuk sama dengan |
| "Pada percabangan bertingkat, semua cabang dijalankan" | Hanya cabang pertama yang cocok |
| "Flowchart yang benar hanya satu gambar" | Banyak gambar dapat setara |

## 6. Latihan terbimbing (`mod-w08.prac-02`, tidak dinilai)

1. Bentuk apa untuk `Output total`?
2. Pada tabel diskon, output untuk total = 250000?
3. Pada aturan emas/perak/perunggu, poin = 1000 → ?

## 7. Cek pemahaman (tidak dinilai)

- Mengapa urutan pemeriksaan penting pada percabangan bertingkat?

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. Jajar genjang.
2. 230000.
3. "emas" (1000 ≥ 1000).

Cek pemahaman: poin 1200 juga ≥ 500; bila pemeriksaan perak didahulukan,
hasilnya salah.

## Ringkasan

- Oval, jajar genjang, persegi panjang, belah ketupat, panah.
- Tabel blok = flowchart: bentuk, isi, blok berikutnya.
- Percabangan bertingkat: berhenti di cabang pertama yang cocok; uji batas.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Flowchart | flowchart | Diagram alir langkah algoritma |
| Keputusan | decision | Blok pertanyaan Ya/Tidak |
| Cabang | branch | Jalur setelah keputusan |
| Bertingkat | nested | Keputusan di dalam cabang keputusan lain |
