---
module_id: mod-w03
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24, CB-1. Belum direview ChatGPT; belum diterima owner"
---

# W3 — Review Kualitas, Kesetaraan Varian, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai |
|---|---|
| Dokumentasi diproduksi | **YA** (CB-1) |
| Review mandiri penyusun | **YA** (dokumen ini) |
| Review ChatGPT | **BELUM** |
| Diterima owner | **BELUM** |
| Runtime diverifikasi | Tidak berlaku / tidak diklaim (tanpa runtime, tanpa jaringan nyata) |
| Durasi diuji dengan pelajar | **TIDAK** |

## 2. Inventaris (dihitung dari berkas)

| Bagian | Jumlah |
|---|---|
| Pelajaran / set latihan | 4 / 4 (40 + 55 + 45 + 40 = 180 menit) |
| Soal teori | **40** (20 slot × 2) |
| Soal concept | **12** (6 slot × 2) |
| Spesifikasi lab | **6** (3 aktivitas × 2) |
| Mini-project | **1** (rubrik MR-A, 17 contoh reviewer) |
| Materi remedial | 6 bagian (R-NET, R-IP, R-SUBNET, R-PROTO, R-LAYER, R-RATE) |

Pemeriksa dokumen (skrip di luar repositori): **188 ID unik**, 0 duplikat;
kunci di opsi; `distractor_rationale` lengkap; urutan diterima ≠ urutan
tampil; CE-S4 satu-ke-satu; CE-S5 P genap; poin = maksimum; field kanonik;
0 galat.

## 3. Tujuan belajar dan asumsi jaringan

| LO | Kompetensi | Pelajaran | Teori | Lab | Proyek | Concept |
|---|---|---|---|---|---|---|
| LO1 jaringan & perangkat | `comp-w03-net-01` | les-01 | s01–s03 | act-03.c01 | K4.q1 | s01 |
| LO2 IPv4 privat/publik | `comp-w03-ip-01` | les-02 | s04–s07 | act-01 | K2.c01–c06, K4.q2 | s02 |
| LO3 jaringan /24 | `comp-w03-subnet-01` | les-02, les-04 | s08–s11 | act-02 | K1.c01–c11, K4.q3 | s03 |
| LO4 protokol | `comp-w03-proto-01` | les-03 | s12–s14 | act-03.c02–c03 | K1.c02–c06 (DHCP), c12, K4.q4 | s04 |
| LO5 lapisan TCP/IP | `comp-w03-layer-01` | les-03 | s15–s17 | act-03.c04 | K4.q5 | s05 |
| LO6 kecepatan | `comp-w03-rate-01` | les-04 | s18–s20 | act-03.c05–c06 | — (alasan di `module.yaml`) | s06 |

Asumsi yang **tertulis** di pelajaran, stem, `spec.md`, dan YAML
(`network_assumptions`):

| ID | Asumsi | Kenyataan (diungkapkan di pelajaran) |
|---|---|---|
| NA-1 | IPv4 desimal; tanpa nol di depan oktet | Sebagian program membaca `010` sebagai oktal; IPv6 ada tetapi tidak dibahas |
| NA-2 | Privat = RFC 1918; alamat valid lain (bukan `127.x`) = publik | Ada rentang khusus lain (169.254, 100.64, dokumentasi) — **tidak dipakai** di butir bernilai (diperiksa: setiap alamat "publik" lolos `is_global`) |
| NA-3 | Mask hanya `255.255.255.0` | Mask lain butuh hitungan bit (W6) — sengaja tidak memakai materi W6 |
| NA-4 | Rentang DHCP termasuk kedua ujung | Sesuai cara router menuliskan rentang |
| NA-5 | Kecepatan ideal, desimal, tanpa tambahan protokol | Nyata lebih lambat (overhead, sinyal, berbagi) |
| NA-6 | Router rumah = router + switch + access point | Perangkat nyata dapat berbeda |
| NA-7 | Empat lapisan TCP/IP | Model OSI 7 lapisan juga dipakai luas |

Tidak ada materi yang bergantung pada modul berikutnya (biner W6 tidak
dipakai). W1 (bit/byte, desimal) dan W2 (proses, aplikasi) menjadi
prasyarat. Nama domain memakai `.example` (dicadangkan untuk contoh).

## 4. Skor yang dapat dicapai dan aritmetika

### 4.1 Maksimum (QC-01)

| Komponen | Dinyatakan | Dapat dicapai | Bukti |
|---|---|---|---|
| Teori | 56 | **56** | 8 × 2 + 8 × 3 + 4 × 4; setiap kunci/jawaban diterima diverifikasi (§4.3) |
| Lab act-01 / act-02 / act-03 | 30 / 40 / 30 | **30 / 40 / 30** | 10 × 3; 8 × 5; 6 × 5 — setiap pemeriksaan satu jawaban benar terverifikasi |
| Lab komponen | 100 | **100** | 30 + 40 + 30 |
| Proyek | 100 | **100** | E01 dan E02 (batas sah .99/.200/.254) mencapai 100 (simulasi 17/17 cocok) |
| Concept | 21 | **21** | CE-S1 4 + CE-S2 (k 3) 3 + CE-S5 4 + CE-S4 4 + CE-S3 (n 5) 4 + CE-S2 (k 2) 2 |

### 4.2 Durasi teori, XP, jadwal

| Hal | Hasil |
|---|---|
| Komposisi teori | TF-1 × 9 (5 D1, 2 D2, 2 D3 — s01, s03, s04, s12, s15 D1; s13, s14 D2; s07, s17 D3), TF-2 × 2 (D2), TF-3 × 7 (s05, s08, s18 D1; s09, s10, s19 D2; s20 D3), TF-4 × 2 (s11 D3, s16 D2) |
| Rumus A.4 | dasar 9·45 + 2·75 + 7·60 + 2·90 = **1.155**; tambahan 480; S = **1.635** → S_buffer = ⌈1.798,5⌉ = **1.799** → ⌈29,98…⌉ + 2 = **32 menit** |
| Timer teori / review umpan balik | **32** / 45 − 32 = **13** menit; TA-B ⌈48⌉ = **48** menit (di luar nominal) |
| XP | 305 (identitas `mod-w03.*`) |
| Jadwal | 180 + 45 + 90 (25 + 35 + 30) + 90 + 30 + 45 = **480 menit**; sesi saran 240 + 240 |

### 4.3 Verifikasi independen jaringan (W3 wajib)

Setiap alamat, jaringan, broadcast, host, dan klasifikasi dihitung ulang
dengan pustaka standar Python `ipaddress` (bukan dengan aturan penyusun):

| Cakupan | Hasil |
|---|---|
| Lab act-01 (20 alamat): valid/privat/publik | 20/20 cocok; semua alamat "publik" adalah alamat global (bukan rentang khusus) |
| Lab act-02 vA `192.168.20.57`: jaringan `.0`, broadcast `.255`, host `.1`–`.254`; DHCP `.60`–`.139` (80) → **174** di luar DHCP; Ya/Tidak | Cocok |
| Lab act-02 vB `10.4.7.130`: `10.4.7.0`, `10.4.7.255`, `.1`, `.254`; DHCP `.10`–`.59` (50) → **204**; Ya/Tidak | Cocok |
| Teori s04, s06 (validitas/privat), s09, s10 (jaringan/broadcast), s11 (tepat satu perangkat salah per varian), s08 (254/256) | Cocok |
| Concept s02, s03; Pelajaran 2 (4 contoh), latihan, remedial | Cocok |
| Proyek: 153 alamat statis sah (.2–.99, .200–.254); P(153, 5) = **78.485.511.600** rencana bernilai penuh; F5 = 254 − 100 − 1 − 5 = **148** | Cocok (*angka P(153,5) semula salah tulis 78.364.164.400 — terdeteksi pemeriksa dan diperbaiki*) |

Kecepatan (semua bilangan bulat, desimal): s18 24 ÷ 8 = 3, 7 × 8 = 56;
s19 400 × 8 ÷ 20 = 160, 420 × 8 ÷ 30 = 112; s20 1.200 × 8 ÷ 40 = 240 dtk
= 4 mnt, 2.400 × 8 ÷ 160 = 120 dtk = 2 mnt; lab 96 ÷ 8 = 12, 9 × 8 = 72,
750 × 8 ÷ 30 = 200, 900 × 8 ÷ 40 = 180; pelajaran 120, 80, 90, 100;
remedial 8, 48. Arah konversi dua arah (QC-03): Mbps → MB/s (÷ 8) dan
MB/s → Mbps (× 8) diajarkan dan dinilai; dua tingkat (GB → MB → Mb) di
s20 dan Pelajaran 4 contoh 2.

### 4.4 Proyek: contoh reviewer (17/17 cocok dengan evaluator dokumentasi)

| Contoh | K1 | K2 | K3 | Total |
|---|---|---|---|---|
| E01 acuan / E02 batas sah | 60 | 20 | 10 | 100 |
| E04 batas tidak sah `.100` | 55 | 20 | 10 | 95 |
| E09 router `.254` konsisten | 54 | 20 | 10 | 94 |
| E10 perangkat = alamat router | 49 | 20 | 10 | 89 |
| E13 nol di depan oktet | 49 | 18 | 6 | 83 |
| E17 kosong | 0 | 0 | 0 | K4 saja |

### 4.5 Skenario kelulusan (`4200·W = 2250·T + 1680·L + 840·P + 2000·C`; lulus ⇔ ≥ 336.000)

| ID | T/56 | L/100 | P/100 | C/21 | `4200·W` | Hasil |
|---|---|---|---|---|---|---|
| SC-1 | 48 | 85 | 80 | 17 | 352.000 | PASSED (83,80…) |
| SC-2 | 42 | 75 | 80 | 16 | 319.700 | NOT_PASSED (76,11…) |
| SC-3 | 56 | 90 | 95 | 15 | 387.000 | NOT_PASSED (C: 60 < 63) |
| SC-4 | 47 | 80 | 76 | 16 | 335.990 | **NOT_PASSED** (79,9976…; pembulatan 2 desimal akan menampilkan "80,00" — keputusan memakai perbandingan eksak) |
| SC-5 | 24 | 100 | 100 | 15 | 336.000 | NOT_PASSED (W tepat 80; T 96 < 168, C 60 < 63) |
| SC-6 | 42 | 84 | 84 | 18 | 342.180 | PASSED (81,47…; T tepat 75%) |

Pencarian lengkap: dengan semua komponen ≥ 75, W tepat 80 **tidak dapat
dicapai** di W3 (0 kombinasi); SC-4 adalah nilai tertinggi di bawah 80.

## 5. Posisi kunci jawaban

Pilihan tunggal teori, CE-S1, perbaikan CE-S5, K4: **a 7 · b 8 · c 8 · d 8**
(setelah penyeimbangan dari a 6 · b 13 · c 8 · d 4; baris tabel s11 vA dan
s16 vB, serta opsi s04 vB, s07 vA, s14 ditata ulang, kunci tetap benar).
Pilihan ganda: s02 {a,c,d}/{b,c,e}; s06 {a,b,d}/{b,c,e}; concept s02
{a,c,e}/{a,c,d}; s06 {a,c}/{b,c}.

## 6. Matriks kesetaraan varian (QC-04)

| Slot | Kompetensi | Konsep wajib | Tuntutan | Format | Kesulitan | Maks. | Detik | Alasan kesetaraan |
|---|---|---|---|---|---|---|---|---|
| s01 | net | peran perangkat | Mengingat | TF-1 | D1 | 2 | 45 | Opsi sama; A access point, B router |
| s02 | net | LAN/WAN/internet/ISP | Memahami | TF-2 | D2 | 3 | 105 | 5 pernyataan, 3 benar, 2 miskonsepsi (Wi-Fi = internet; internet milik satu pihak / ukuran WAN) |
| s03 | net | klien vs server | Memahami | TF-1 | D1 | 2 | 45 | Opsi sama; A meminta → klien, B menyediakan → server |
| s04 | ip | validitas | Menerapkan | TF-1 | D1 | 2 | 45 | A satu valid di antara 3 tidak valid; B satu tidak valid di antara 3 valid; aturan oktet sama |
| s05 | ip | fakta IPv4 | Mengingat | TF-3 | D1 | 2 | 60 | Satu fakta dasar (255 / 4 oktet) |
| s06 | ip | rentang privat | Menerapkan | TF-2 | D2 | 3 | 105 | 3 privat + 2 jebakan batas (172.40 / 11.x; 172.32 / 192.172) |
| s07 | ip | privat vs publik + NAT | Menganalisis skenario | TF-1 | D3 | 4 | 105 | Kedua skenario rumah dengan router ISP; penalaran privat hanya di LAN |
| s08 | subnet | jumlah alamat /24 | Mengingat | TF-3 | D1 | 2 | 60 | 254 host / 256 seluruhnya |
| s09 | subnet | alamat jaringan | Menerapkan | TF-3 | D2 | 3 | 90 | Satu alamat host → `.0` |
| s10 | subnet | broadcast | Menerapkan | TF-3 | D2 | 3 | 90 | Satu alamat host → `.255` |
| s11 | subnet | konfigurasi perangkat | Menganalisis tabel | TF-4 | D3 | 4 | 150 | 4 perangkat, tepat 1 salah (A gateway di jaringan lain; B alamat broadcast); jebakan alamat batas sah (.254 / .253) |
| s12 | proto | DNS / DHCP | Mengingat | TF-1 | D1 | 2 | 45 | Opsi sama |
| s13 | proto | diagnosis protokol | Menganalisis gejala | TF-1 | D2 | 3 | 75 | Opsi sama; A DNS (nama gagal, IP berhasil), B DHCP (tanpa alamat) |
| s14 | proto | port 80/443, enkripsi, batas HTTPS | Memahami | TF-1 | D2 | 3 | 75 | Opsi sama (4 kombinasi); kedua varian memuat pengecoh "HTTPS menjamin situs jujur" |
| s15 | layer | lapisan protokol | Mengingat | TF-1 | D1 | 2 | 45 | Opsi sama; A internet, B transport |
| s16 | layer | pemetaan ke lapisan | Menerapkan tabel | TF-4 | D2 | 3 | 120 | 4 baris, tepat 1 salah (DNS → transport / access point → internet) |
| s17 | layer | lapisan dari gejala | Menganalisis | TF-1 | D3 | 4 | 105 | A bawah (fisik), B atas (aplikasi); kedua stem memberi bukti lapisan lain berjalan |
| s18 | rate | konversi satu arah | Menerapkan | TF-3 | D1 | 2 | 60 | A ÷ 8, B × 8 (dua arah) |
| s19 | rate | waktu transfer | Menerapkan | TF-3 | D2 | 3 | 90 | MB × 8 ÷ Mbps, hasil bulat |
| s20 | rate | GB → MB → Mb → detik → menit | Menerapkan 3 langkah | TF-3 | D3 | 4 | 120 | Langkah sama; hasil menit bulat |

| Slot | Kompetensi | Konsep wajib | Format | Maks. | Alasan kesetaraan |
|---|---|---|---|---|---|
| concept.s01 | net | LAN vs internet; router; switch | CE-S1 | 4 | A: mengapa LAN jalan tanpa internet; B: mengapa butuh router — keduanya membedakan di-dalam-LAN vs antarjaringan |
| concept.s02 | ip | rentang privat; publik dari ISP; NAT | CE-S2 (k 3) | 3 | 3 benar + 2 pengecoh (privat dapat dihubungi/unik; batas rentang atau alamat tidak valid) |
| concept.s03 | subnet | jaringan, broadcast, 254, satu jaringan | CE-S5 (P 4) | 4 | Satu baris salah di antara 4 fakta /24 yang benar |
| concept.s04 | proto | DHCP, DNS, HTTP/HTTPS, TCP/UDP | CE-S4 (k 4, r 5) | 4 | 4 protokol + 1 pengecoh = fungsi protokol pasangan (TCP/UDP) |
| concept.s05 | layer | urutan lapisan, bungkus/buka | CE-S3 (n 5) | 4 | A mengirim (atas → bawah), B menerima (bawah → atas); 5 langkah; 1 urutan diterima |
| concept.s06 | rate | × 8; ideal vs nyata | CE-S2 (k 2) | 2 | Satu konversi + satu batas model di kedua varian |

| Aktivitas | Konsep | Maks. | Menit | Bukti kesetaraan |
|---|---|---|---|---|
| act-01 | valid/privat/publik | 30 | 25 | Distribusi sama P 4 · U 3 · X 3; jebakan batas 172.16/172.32 (A) dan 172.31/172.15 (B); 3 oktet dan > 255 di keduanya |
| act-02 | /24 | 40 | 35 | Struktur sama; rentang DHCP berbeda (80 vs 50); Ya/Tidak memuat 1 sah, 1 jaringan lain, 1 tidak valid (urutan berbeda) |
| act-03 | perangkat, protokol, port, lapisan, kecepatan | 30 | 30 | Pasangan per nomor setara (router/AP; DHCP/DNS; 443/80; lapisan bawah/atas; ÷ 8 / × 8; waktu) |

## 7. Tumpang-tindih dan visibilitas (QC-06, QC-11)

| Temuan pemindaian | Tindakan |
|---|---|
| act-02 pertanyaan Ya/Tidak memuat `192.168.20.255` (= jawaban c02) dan `10.4.7.0` (= jawaban c01) | **Diperbaiki**: diganti alamat tidak valid `192.168.20.256` dan `10.4.7.300` |
| `254`, `255`, `256`, `443` muncul di pelajaran | Diterima: fakta yang diajarkan dan diuji sebagai ingatan (s05, s08, act-03 c03) |
| `192.168.20.1` sebagai substring `192.168.20.139` | Positif palsu |

Angka dan alamat pelajaran/latihan/remedial (192.168.5.42, 10.20.30.40,
172.18.4.99, 172.27.8.66, 172.20.9.0 dengan DHCP .50–.149, 192.168.88.0;
16↔2, 600 MB/40, 1 GB/100, 450 MB/40, 48 Mbps, 200 MB/16, 64 Mbps,
90 MB/15) berbeda dari semua butir bernilai **beserta hasilnya**. Contoh
proyek memakai jaringan `10.9.8.0/24` dan angka bentuk `57`.

## 8. QC-01–QC-12 dan CQ-01–CQ-20

| QC | Hasil | Bukti |
|---|---|---|
| QC-01 | PASS | §4.1 |
| QC-02 | PASS | §4.4 (17/17), §4.5 |
| QC-03 | PASS | §4.3 kecepatan dua arah + dua tingkat |
| QC-04 | PASS | §6 |
| QC-05 | PASS | §3 NA-1–NA-7 |
| QC-06 | PASS setelah perbaikan | §7 |
| QC-07 | PASS | `spec.md` ↔ `checks.yaml` (alamat, rentang, pertanyaan, poin); proyek N1–N5 ↔ rubrik |
| QC-08 | PASS | Normalisasi alamat (tanpa nol depan, `/24` ditolak di lab, dibaca di proyek dengan kehilangan K3), angka + satuan, Ya/Tidak; `depends_on` |
| QC-09 | PASS | Field kanonik |
| QC-10 | PASS | Batas `.99/.100/.199/.200/.254/.255`, `172.15/16/31/32`; SC-4 |
| QC-11 | PASS setelah perbaikan | §7 |
| QC-12 | PASS | Desimal dinyatakan di setiap butir kecepatan; tidak ada satuan biner |

CQ-01–CQ-20: PASS (kebenaran teknis diverifikasi dengan `ipaddress`;
ramah pemula; LO terukur; prasyarat W1–W2; cakupan §3; tidak menilai materi
W6; kelengkapan §2; kesetaraan §6; kunci; aritmetika §4.3; fixture
deterministik; rubrik objektif; concept D-23; XP unik; aksesibilitas —
setiap diagram/tabel inti dideskripsikan; versi 1.0; 480 menit; offline;
konsistensi D-01–D-38; kunci tidak tampil sebelum umpan balik).

## 9. Regresi F-01–F-23

| Temuan W1 | Pemeriksaan di W3 | Status |
|---|---|---|
| F-01/F-02/F-19 | F5 punya pemeriksaan kebenaran (K1.c12); K2 bentuk saja; MR-2 per pemeriksaan | PASS |
| F-03 | §5 | PASS |
| F-04/F-12/F-13 | §6 | PASS |
| F-05/F-21 | §4.3 (jumlah rencana sah dihitung, galat salah tulis diperbaiki) | PASS |
| F-07/F-14/F-23 | §7 | PASS setelah perbaikan |
| F-09 | §4.1 | PASS |
| F-10/F-22 | Konversi dua arah; desimal | PASS |
| F-11/F-15 | §3 asumsi di stem (s07, s11, s19, s20) dan `spec.md` | PASS |
| F-16/F-20 | Field kanonik; `normalization` per aktivitas | PASS |
| F-17 | Label perangkat; "dapat menjadi alamat perangkat lain di jaringan yang sama" didefinisikan | PASS |
| F-24–F-27 | `.claude/` tidak disentuh | Dipertahankan |

## 10. Batas penilaian objektif dan bukti reviewer

Pemeriksaan membuktikan jawaban sesuai aturan model W3; tidak membuktikan
kemampuan mengonfigurasi perangkat nyata (D-17, D-34). Tidak ada lab yang
meminta akses jaringan nyata.

| Field | Isi |
|---|---|
| Reviewer / tanggal / basis | Claude (penyusun), 2026-11-24, `main` = `ab0103e` |
| Temuan terbuka | Tidak ada yang diketahui; butuh review ChatGPT dan penerimaan owner |

Metrik W3 (dari transkrip; ±2): panggilan alat ≈ 25; berkas baru yang
dibaca untuk persiapan 0 (bukti dan acuan W2/W1 dipakai ulang, TE-13); baca
ulang 0; aksi gagal 0; temuan pemeriksa yang benar 3 (kebocoran act-02,
bias kunci, salah tulis P(153,5)); kegagalan identik berulang 0; aktivasi
skill 0 tambahan; checkpoint 1; operasi validasi 8; **pemulihan sesi 1**
(worker dimulai ulang di tengah W3 — dilanjutkan dari berkas di branch dan
`git status` tanpa mengulang pekerjaan). TOKEN USAGE: **NOT MEASURABLE**.
