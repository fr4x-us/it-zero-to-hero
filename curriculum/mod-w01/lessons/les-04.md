---
lesson_id: mod-w01.les-04
practice_id: mod-w01.prac-04
module_id: mod-w01
content_version: "1.0"
title: "Membaca Spesifikasi, Kompatibilitas, dan Memilih Komputer Sesuai Kebutuhan"
language: id
duration_minutes: 45        # materi 30 + latihan terbimbing 15
competencies: [comp-w01-spec-01, comp-w01-unit-01, comp-w01-cpu-01]
prerequisites: [mod-w01.les-02, mod-w01.les-03]
accessibility:
  tables_with_core_data: [tbl-w01-04-katalog]
  english_terms: [specification, socket, compatibility, DDR4, DDR5, slot, watt, budget]
---

# Pelajaran 4 — Spesifikasi dan Kompatibilitas

## Tujuan pelajaran

1. Membaca tabel spesifikasi komponen (core, GHz, kapasitas, jenis RAM,
   watt, harga).
2. Memeriksa **kompatibilitas** CPU–motherboard (soket) dan RAM–motherboard
   (jenis DDR, jumlah slot).
3. Menghitung kebutuhan daya dengan aturan belajar W1 dan total harga.
4. Memilih kombinasi komponen yang memenuhi kebutuhan **dan** anggaran.

## Mengapa ini penting?

Komponen yang bagus tidak berguna bila **tidak cocok** satu sama lain. CPU
yang tidak sesuai soket motherboard tidak dapat dipasang. Kemampuan membaca
spesifikasi juga melatih cara berpikir sistematis: menguji setiap syarat
satu per satu — keterampilan yang sama dipakai saat menguji program.

## 1. Kompatibilitas

**Kompatibel** artinya komponen dapat dipasang dan bekerja bersama.

| Pasangan | Syarat | Contoh tidak kompatibel |
|---|---|---|
| CPU ↔ motherboard | **Soket** CPU sama dengan soket motherboard | CPU Soket A di motherboard Soket B |
| RAM ↔ motherboard | **Jenis RAM** sama (DDR4 atau DDR5); jumlah keping ≤ **slot** RAM | RAM DDR5 di motherboard DDR4 |
| PSU ↔ seluruh komponen | Daya PSU ≥ kebutuhan daya | PSU 200 W untuk kebutuhan 245 W |

DDR4 dan DDR5 memiliki bentuk dan takik berbeda sehingga tidak dapat saling
menggantikan. Nama soket nyata contohnya AM5 atau LGA1700; di modul ini
dipakai nama umum **Soket A** dan **Soket B**.

**Model kompatibilitas W1 vs kenyataan.** Di modul ini, komponen dianggap
kompatibel bila soket sama, jenis RAM sama, jumlah keping ≤ slot, dan daya
PSU cukup — aturan untuk **katalog fiktif** latihan. Pada perangkat keras
nyata, soket yang sama **belum menjamin** kecocokan: chipset motherboard,
versi firmware (BIOS/UEFI) yang mendukung CPU tersebut, dan daftar
kompatibilitas dari produsen juga menentukan. Hal itu tidak dinilai di W1.

**Aturan belajar W1 untuk daya** (model latihan, **bukan** standar teknik
atau panduan membeli PSU; kebutuhan nyata dihitung dari semua komponen dan
cadangan):

```
kebutuhan daya (W) = daya CPU (W) + 100 W untuk komponen lain
PSU memenuhi bila  : daya PSU ≥ kebutuhan daya
```

## 2. Membaca kebutuhan pengguna

Kebutuhan ditulis sebagai syarat yang dapat diperiksa:

| Kebutuhan | Cara memeriksa |
|---|---|
| "Minimal 6 core" | core ≥ 6 |
| "RAM minimal 16 GB" | kapasitas per keping × jumlah keping ≥ 16 |
| "SSD minimal 512 GB" | jenis = SSD **dan** kapasitas ≥ 512 |
| "Anggaran Rp 6.000.000" | total harga ≤ 6.000.000 |

## 3. Contoh terbimbing lengkap

Katalog contoh (harga fiktif untuk latihan):

<a id="tbl-w01-04-katalog"></a>

| ID | Jenis | Spesifikasi | Daya | Harga (Rp) |
|---|---|---|---|---|
| X-CPU1 | CPU | Soket A, 4 core, 3,8 GHz | 65 W | 1.700.000 |
| X-CPU2 | CPU | Soket B, 8 core, 4,1 GHz | 105 W | 3.600.000 |
| X-MB1 | Motherboard | Soket A, DDR4, 2 slot | — | 1.200.000 |
| X-MB2 | Motherboard | Soket B, DDR5, 4 slot | — | 2.000.000 |
| X-RAM1 | RAM | DDR4, 8 GB per keping | — | 340.000 |
| X-RAM2 | RAM | DDR5, 8 GB per keping | — | 440.000 |
| X-SSD1 | Penyimpanan | SSD 512 GB | — | 640.000 |
| X-PSU1 | PSU | 300 W | — | 360.000 |

*Deskripsi tabel tbl-w01-04-katalog:* delapan komponen dengan jenis,
spesifikasi, daya, dan harga; dipakai pada contoh di bawah.

**Kebutuhan:** komputer belajar dengan minimal 4 core, RAM minimal 16 GB,
SSD minimal 512 GB, anggaran Rp 4.500.000.

**Langkah 1 — pilih CPU dan motherboard yang sesoket.** X-CPU1 (Soket A)
cocok dengan X-MB1 (Soket A). X-CPU2 (Soket B) cocok dengan X-MB2.

**Langkah 2 — pilih RAM sesuai jenis dan slot.** X-MB1 memakai DDR4 dan
punya 2 slot → X-RAM1 × 2 = 16 GB. (X-RAM2 adalah DDR5 → tidak cocok.)

**Langkah 3 — penyimpanan.** X-SSD1 adalah SSD 512 GB → memenuhi.

**Langkah 4 — daya.** Kebutuhan = 65 + 100 = 165 W; X-PSU1 300 W ≥ 165 →
memenuhi.

**Langkah 5 — harga.**

| Komponen | Harga (Rp) |
|---|---|
| X-CPU1 | 1.700.000 |
| X-MB1 | 1.200.000 |
| X-RAM1 × 2 | 680.000 |
| X-SSD1 | 640.000 |
| X-PSU1 | 360.000 |
| **Total** | **4.580.000** |

Total 4.580.000 **melebihi** anggaran 4.500.000 → kombinasi ini **tidak**
memenuhi kebutuhan, walaupun semuanya kompatibel. Pilihan lain dengan
X-CPU2 lebih mahal lagi. Kesimpulan: dengan katalog ini kebutuhan tidak
dapat dipenuhi; pengguna perlu menambah anggaran atau mengurangi syarat.
Pelajaran: **periksa setiap syarat, termasuk anggaran, sampai akhir.**

## 4. Memilih sesuai kebutuhan

| Kebutuhan pengguna | Komponen yang paling berpengaruh |
|---|---|
| Banyak aplikasi/tab terbuka bersamaan | RAM cukup besar; CPU dengan beberapa core |
| Membuka program dan berkas dengan cepat | SSD |
| Menyimpan banyak video dengan biaya rendah | HDD berkapasitas besar (lebih murah per GB) sebagai penyimpanan tambahan |
| Mengolah grafis berat | GPU yang kuat |

## 5. Miskonsepsi umum

| Miskonsepsi | Yang benar |
|---|---|
| "Komponen termahal pasti cocok." | Kecocokan ditentukan soket, jenis RAM, slot, dan daya, bukan harga |
| "RAM DDR5 bisa dipasang di mana saja karena lebih baru." | Hanya di motherboard yang mendukung DDR5 |
| "PSU berapa pun cukup asalkan komputer menyala." | Daya PSU harus ≥ kebutuhan |
| "Cukup memenuhi sebagian besar syarat." | Kombinasi memenuhi kebutuhan hanya bila **semua** syarat terpenuhi |

## 6. Latihan terbimbing (`mod-w01.prac-04`, tidak dinilai)

Memakai katalog contoh di atas:

1. Apakah X-CPU2 kompatibel dengan X-MB1? Mengapa?
2. Hitung RAM total untuk X-RAM2 × 4 dan sebutkan motherboard yang cocok.
3. Hitung kebutuhan daya untuk X-CPU2 dan tentukan apakah X-PSU1 cukup.
4. Bila anggaran naik menjadi Rp 4.600.000, apakah kombinasi contoh
   terbimbing memenuhi kebutuhan?

## 7. Cek pemahaman (tidak dinilai)

- Mengapa kombinasi yang semuanya kompatibel masih bisa "tidak memenuhi"?
- Sebutkan tiga pemeriksaan kompatibilitas di modul ini.

## Pembahasan latihan (ditampilkan setelah pelajar mencoba)

1. Tidak; X-CPU2 Soket B, X-MB1 Soket A.
2. 4 × 8 GB = 32 GB; X-MB2 (DDR5, 4 slot).
3. 105 + 100 = 205 W; 300 W ≥ 205 W → cukup.
4. Ya; 4.580.000 ≤ 4.600.000 dan syarat lain terpenuhi.

## Ringkasan

- Kompatibel = soket CPU sama dengan motherboard, jenis RAM sama, jumlah
  keping ≤ slot, daya PSU ≥ kebutuhan.
- Kebutuhan ditulis sebagai syarat yang dapat diperiksa satu per satu.
- Kombinasi memenuhi hanya bila **semua** syarat dan anggaran terpenuhi.

## Glosarium

| Istilah | Bahasa Inggris | Arti |
|---|---|---|
| Spesifikasi | specification | Data teknis komponen |
| Soket | socket | Tempat CPU dipasang di motherboard |
| Kompatibel | compatible | Dapat dipasang dan bekerja bersama |
| DDR4/DDR5 | DDR4/DDR5 | Generasi RAM yang tidak saling menggantikan |
| Slot | slot | Tempat memasang keping RAM |
| Watt | watt (W) | Satuan daya listrik |
| Anggaran | budget | Batas biaya |
