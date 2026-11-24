---
module_id: mod-w03
content_version: "1.0"
template: TPL-19, TPL-20
review_type: "Review dokumentasi oleh penyusun (Claude), 2026-11-24, CB-1 + koreksi F-28–F-72 (dua putaran). Review independen PR #27: REQUEST CHANGES (dua kali) → dikoreksi; re-review BELUM; belum diterima owner"
---

# W3 — Review Kualitas, Kesetaraan Varian, dan Bukti

## 1. Status (dibedakan tegas)

| Status | Nilai |
|---|---|
| Dokumentasi diproduksi | **YA** (CB-1) |
| Review mandiri penyusun | **YA** (dokumen ini) |
| Review independen (ChatGPT) | PR #27: **REQUEST CHANGES** (F-28–F-70, lalu delta F-28–F-72) → dikoreksi; **re-review BELUM** |
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
| Proyek | 100 | **100** | E01 dan E02 (batas sah .99/.200/.254) mencapai 100 (simulasi 21/21 cocok) |
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

### 4.4 Proyek: contoh reviewer (21/21 cocok setelah koreksi dengan evaluator dokumentasi)

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
| QC-02 | PASS | §4.4 (21/21), §4.5 |
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
| Temuan terbuka | Tidak ada BLOCKED (deskripsi F-55–F-57, F-59 dipulihkan owner, putaran 2); butuh re-review independen dan penerimaan owner. Register: bagian koreksi konsolidasi di akhir dokumen |

Metrik W3 (dari transkrip; ±2): panggilan alat ≈ 25; berkas baru yang
dibaca untuk persiapan 0 (bukti dan acuan W2/W1 dipakai ulang, TE-13); baca
ulang 0; aksi gagal 0; temuan pemeriksa yang benar 3 (kebocoran act-02,
bias kunci, salah tulis P(153,5)); kegagalan identik berulang 0; aktivasi
skill 0 tambahan; checkpoint 1; operasi validasi 8; **pemulihan sesi 1**
(worker dimulai ulang di tengah W3 — dilanjutkan dari berkas di branch dan
`git status` tanpa mengulang pekerjaan). TOKEN USAGE: **NOT MEASURABLE**.

## 11. Koreksi konsolidasi CB-1 (PR #27, F-28–F-70; 2026-11-24)

Review PR #27 = **REQUEST CHANGES**. Sebelum mengedit diverifikasi: head
`a9241d33c2cf32e177ca92618df458b78dd6cb98`, base
`ab0103e4954ead4ded6343d105d73a2729916cd6` (cocok). Koreksi diterapkan pada
PR #27 yang sama. Status modul: **diproduksi dan dikoreksi; menunggu re-review
independen dan penerimaan owner** — belum diterima.

### 11.1 Register F-28–F-72 (45 ID; diperbarui pada koreksi terarah putaran 2)

| ID | Lingkup | Disposisi | Bukti |
|---|---|---|---|
| F-28 | W3 ◀ | CONFIRMED — FIXED | `project/rubric.yaml` K1.c02–c06 membandingkan dengan konstanta `192.168.50.1` (bukan isian F1) + `f1_dependency`; F1 salah tidak lagi menjatuhkan pemeriksaan lain; fixture E18–E21 |
| F-29 | W4 | CONFIRMED — FIXED | `lab/act-02` `verdict_rule`: A = tidak ada indikator dalam model W4, **bukan** jaminan aman; spesifikasi diselaraskan |
| F-30 | W4 | CONFIRMED — FIXED | act-01 vA S6 + halaman yang meminta sandi email (bukti perilaku fiktif); label `WIF` = bukti perilaku; les-01: nama mirip saja bukan bukti; proyek S4 diperkuat |
| F-31 | W3 ◀ | NOT REPRODUCED | Blueprint dan review W3 pada commit produksi awal `9a562ce` dan pada head koreksi: TF-3 = 7 slot (s05, s08, s09, s10, s18, s19, s20) di keduanya; review mencantumkan "TF-3 × 7" di keduanya (dihitung ulang dari `git show`) |
| F-32 | W2 | CONFIRMED — FIXED | theory s05 vB dan concept s02 vA menyatakan "tidak punya simpan otomatis/pemulihan"; les-02 menjelaskan pengecualian simpan otomatis |
| F-33 | W2 | CONFIRMED — FIXED | theory s09 vA opsi a; concept s03 vA opsi d + umpan balik isi/ekstensi/pengaitan; les-03 membedakan isi, ekstensi, pengaitan aplikasi |
| F-34 | W3 ◀ | CONFIRMED — FIXED | theory s01 vA/vB dan act-03 c01: "Model peran W3 … **fungsi**" + rasional kotak router Wi-Fi; les-01 fungsi vs kotak |
| F-35 | W3 ◀ | CONFIRMED — FIXED | concept s04 (R5/R2): TCP mengirim ulang data hilang dan menyusun berurutan **selama sambungan berjalan**; les-03 diselaraskan |
| F-36 | W4 | CONFIRMED — FIXED | concept s04 opsi/umpan balik: HTTPS = sambungan terenkripsi ke nama domain, bukan bukti organisasi/kejujuran; les-03 tabel empat pertanyaan; remedial R-PHISH |
| F-37 | W4 | CONFIRMED — DOCUMENTATION CLARIFIED | Klarifikasi asumsi skenario (putaran 2): stem menyatakan model hentikan → amankan dan A prasyarat B; dua urutan diterima per varian **bukan** cacat. Isi putaran 1: concept s06 vA ditulis ulang: model "hentikan → amankan" dinyatakan di stem; A prasyarat B; 2 urutan diterima (ABCD, ABDC) — setara dengan vB (2 urutan); petunjuk "Setelah …" yang membocorkan urutan dihapus |
| F-38 | W4 | CONFIRMED — FIXED | s09/s11, act-03 c03, concept s03, les-02, remedial: digit 0–9, boleh diawali 0 dan berulang, yang dihitung jumlah PIN berbeda; jawaban diverifikasi `10**n` |
| F-39 | W4 | CONFIRMED — FIXED | `collection_validity` (kode tak dikenal/ganda → koleksi INVALID, pemeriksaan yang bergantung 0, lainnya tetap); fixture E14–E17 |
| F-40 | W2 | CONFIRMED — FIXED | `tree_valid` (6 syarat); pohon rusak → pemeriksaan bergantung F1 = 0, K2.c02–c05 tetap; gangguan aplikasi → EVALUATION_ERROR; fixture E17–E20 |
| F-41 | W2 | CONFIRMED — FIXED | act-01: "jenis isi yang **diharapkan** dari ekstensi"; umpan balik "→ diharapkan …"; les-03: ekstensi bukan bukti isi |
| F-42 | W2–W4 ◀ | CONFIRMED — FIXED | Aturan normalisasi eksplisit di setiap TF-3 dan lab (nol di depan ditolak; pemisah ribuan hanya bila diizinkan, pola `1.234`); `normalization_examples` di checks lab; diperiksa konsisten otomatis |
| F-43 | W3 ◀ | CONFIRMED — FIXED | act-01 `network_assumptions` menyebut rentang khusus (loopback, link-local, dll.) di luar model; les-02: publik "umumnya unik"; status publik hanya dari fixture |
| F-44 | W4 | CONFIRMED — FIXED | les-02: pembatasan percobaan PIN menurunkan risiko, **tidak** membuat tebakan mustahil; MFA "jauh lebih sulit", bukan mustahil |
| F-45 | W2 | CONFIRMED — DOCUMENTATION CLARIFIED | `final_state_only`: hanya keadaan akhir pohon dinilai; spesifikasi N4; fixture E21 (dihapus lalu dipulihkan → 100) |
| F-46 | W3 ◀ | CONFIRMED — DOCUMENTATION CLARIFIED | `suffix_24_rule` dan catatan IPN (lab vs proyek); fixture E20 (F1 `/24`) |
| F-47 | W4 | CONFIRMED — DOCUMENTATION CLARIFIED | T1 diberi catatan "aturan simulasi"; les-02: panjang saja tidak cukup (sandi umum/bocor tetap lemah) |
| F-48 | W2 | CONFIRMED — DOCUMENTATION CLARIFIED | s19 vB rasional = model W2; les-04 membedakan model tulis/hapus W2 dari izin folder nyata |
| F-49 | W3 ◀ | CONFIRMED — FIXED | Putaran 2 (deskripsi asli): s07 vA opsi a dan pembahasan tidak lagi menganggap router pasti beralamat publik; alamat privat tidak dirutekan langsung di internet publik; CGNAT disebut; vB menyatakan skenario tanpa CGNAT; les-02 diselaraskan. Kunci tetap a/c. Koreksi putaran 1 dipertahankan: les-02: alamat IP milik **antarmuka**, bukan perangkat |
| F-50 | W3 ◀ | CONFIRMED — FIXED | Putaran 2: s13 vA memberi asumsi (halaman sama tanpa peringatan sertifikat; pesan "alamat server untuk nama itu tidak ditemukan"); rasional HTTPS dan pembahasan menyebut DNS sebagai dugaan terkuat, bukan bukti pasti. Kunci tetap b. Putaran 1 dipertahankan: les-03 cek pemahaman: DNS/IP "kadang" (cache, alamat langsung) — tidak dinyatakan selalu |
| F-51 | W3 ◀ | CONFIRMED — FIXED | Putaran 2 (koreksi penilaian): satuan kecepatan peka huruf — s18 (`NUMR`, normalization_examples), lab act-03 c05 (head lama menerima `12 mb/s` dan `12 Mb/s`), spesifikasi lab, les-04; 8 fixture owner + 107 contoh lolos `norm_check.py`. Putaran 1 dipertahankan: les-04: reservasi DHCP sebagai alternatif alamat statis di luar rentang; aturan RA tidak berubah |
| F-52 | W4 | CONFIRMED — FIXED | Putaran 2: aturan kategori utama dijadikan **berurutan** (aturan pertama yang cocok) karena WIF dan PHI tumpang-tindih pada Wi-Fi tiruan yang menampilkan halaman peminta sandi (act-01 vA S6, vB S7; proyek S4); kunci tidak berubah, setiap skenario tepat satu kunci. Putaran 1: Aturan **kategori utama** (s07 stem, act-01 `primary_classification_rule`, proyek Bagian A, les-01); s07 vB E2 diperjelas |
| F-53 | W4 | CONFIRMED — FIXED | Putaran 2: s08 vB pembahasan, concept s01 (R2, L4) dan s03 vB baris 3, les-02, remedial: OTP = bukti sementara akses ke autentikator/rahasianya, dapat dicuri/diteruskan; tanpa klaim "membuktikan pemilik/memegang ponsel". Putaran 1 (rumusan "bukti memegang ponsel" kini diganti): s08 vB; concept s03 baris autentikator; les-02: autentikasi = pembuktian, OTP = faktor "yang dimiliki" |
| F-54 | W4 | CONFIRMED — FIXED | Putaran 2: s16 vA/vB pembahasan mendefinisikan lima jenis media model W4 (CB-2) dan menghitung media tiap rencana; folder lain di perangkat sama bukan media baru. Kunci dan aturan 3-2-1 tetap. Putaran 1: les-04 CB-1 "salinan terpisah"; model W4 menganggap salinan utuh, dunia nyata perlu uji pemulihan; aturan 3-2-1 dan penilaian tidak berubah |
| F-55 | W4 | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner (putaran 2): s19 vA kini menyatakan Nia masih dapat masuk dengan sandi lama dari perangkat aman; pembahasan menyebut urutan berlaku untuk skenario ini (bila akses hilang: pemulihan lewat kanal resmi; melapor sedini mungkin). Urutan tetap tunggal BDAC |
| F-56 | W2 | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner: concept s04 vB opsi d `../../foto/sampul.png` mencapai tujuan tetapi bukan terpendek. Diperbaiki di putaran 1 (baris salah menuntut "path relatif **terpendek**"; rasional d). Inspeksi independen terarah: PASS; dipertahankan |
| F-57 | W2 | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner (putaran 2): concept s05 vB langkah B kini memeriksa jumlah/nama berkas **dan** membuka setiap berkas untuk memastikan isinya lengkap dan terbaca sebelum menghapus asal (tanpa hash); umpan balik dan les-04 diselaraskan. Format CE-S3 dan urutan ABCD tetap |
| F-58 | W4 | CONFIRMED — FIXED | Putaran 2 (deskripsi asli): concept s01 vB L2 "dibaca orang lain **tanpa izin pemiliknya**"; skenario CIA terkait diperketat (s01 vB L1, theory s02 vB K2/K3/K4, s03 vB). Koreksi putaran 1 tentang tanda vs bukti malware dipertahankan sebagai koreksi tambahan, bukan pengganti: s05 stem: gejala = **tanda peringatan**, bukan bukti pasti; klasifikasi unik hanya dengan bukti perilaku fiktif (act-01, les-01) |
| F-59 | W4 | CONFIRMED — FIXED | Deskripsi asli dipulihkan owner (putaran 2): label AMN = tindakan pengguna tepat / bukti ancaman tidak cukup, **bukan** jaminan tidak ada ancaman — spec, checks (`codes`, `primary_classification_rule`), skenario vB S10 (yang diklasifikasikan = tindakan memeriksa lewat aplikasi resmi), umpan balik. ID AMN dan poin tetap |
| F-60 | W2 | CONFIRMED — FIXED | les-01: "aplikasi biasa" berjalan di atas OS + catatan perangkat tanpa OS (bare-metal) |
| F-61 | W2 | CONFIRMED — FIXED | les-02 latihan 1c: satu aplikasi dapat punya dua proses (dua PID) + pembahasan; jendela ≠ proses |
| F-62 | W3 ◀ | CONFIRMED — FIXED | les-01: modem vs ONT/ONU (fiber) |
| F-63 | W3 ◀ | CONFIRMED — FIXED | les-03: contoh TCP/UDP sebagai "pemakaian umum" + catatan QUIC (HTTP/3 di atas UDP) |
| F-64 | W3 ◀ | CONFIRMED — FIXED | les-04: RA-5 (gateway) berlaku untuk klien LAN |
| F-65 | W4 | CONFIRMED — FIXED | Inspeksi independen terarah PASS; dipertahankan (pengecualian `@`, port, `?`, `#`). les-03: UR-1 hanya untuk bentuk alamat W4 (tanpa port, userinfo, alamat IP) |
| F-66 | W4 | CONFIRMED — FIXED | les-04 dan concept s06: laporkan sedini mungkin (boleh bersamaan); tidak harus menunggu langkah terakhir |
| F-67 | W2–W4 ◀ | CONFIRMED — FIXED | Remedial W2–W4: VA-1–VA-6 (pemakaian paling sedikit → bukan varian sebelumnya → indeks terkecil; VA-3) |
| F-68 | W4 | CONFIRMED — FIXED | Remedial R-AUTH: MFA = **dua faktor atau lebih** dari jenis berbeda |
| F-69 | docs | CONFIRMED — FIXED | `CURRICULUM_PRODUCTION_PLAN.md` header/legenda/§4/§6.1 (historis)/§8; `CURRICULUM_OFFLINE_LAB_SPEC.md` K-13 historis + status aktif |
| F-70 | docs | CONFIRMED — FIXED | Baris CB-0: semua kebijakan terputuskan, tanpa penerimaan terpisah, review independen terbatas, **bukan** final global; CB-1a ACCEPTED (W01-ACC) |
| F-71 | W2 | CONFIRMED — FIXED | Baru (putaran 2): setiap depends_on yang memakai F1 kini `F1 (tree_valid)`, termasuk K1.c11–c14 (head lama tanpa F1); dependency_rule diperjelas. `sim_w02.py`: 19 pemeriksaan bergantung tree_valid, independen tepat K2.c02–c05; E17–E20 = 0/16/0 · 26; E21 = 100 |
| F-72 | W4 | CONFIRMED — FIXED | Baru (putaran 2): depends_on K1.c01–c17, K2.c01–c06, K3.c01–c03 mensyaratkan isian sah (collection_validity); K2.c07–c08 tetap independen; akun tak dikenal dan struktur luar rusak diperjelas dengan kontrak yang ada; fixture E19, E20; `sim_w04.py` 34 asersi dependensi + uji mutasi |

Ringkasan (45 ID, satu disposisi per ID; bukan 45 cacat aktif): FIXED 39 · NOT REPRODUCED 1 · DOCUMENTATION CLARIFIED 5. ◀ = berlaku untuk modul ini.

### 11.2 Matriks bukti per butir

Kolom 1–10 = kriteria re-audit: 1 kompetensi/LO · 2 akurasi akademik ·
3 asumsi model eksplisit · 4 kunci benar dan tunggal · 5 pengecoh sah ·
6 skor deterministik · 7 maksimum tercapai · 8 kesetaraan varian ·
9 umpan balik · 10 visibilitas. **A** = diperiksa otomatis (pemeriksa
struktur: ID unik, kunci di opsi, rasional per pengecoh, poin, kompetensi;
pemindai V-L); **S** = jawaban dihitung ulang independen (simulasi, mis.
`ipaddress`, `urlsplit`, `10**n`); **M** = dibaca manual oleh penyusun;
— = tidak berlaku. Semua sel lolos pada putaran ini; kolom "Koreksi" =
temuan yang menyentuh butir itu. Ini review mandiri, bukan review independen.

| Butir | Komp. | Format · D | Kunci vA / vB | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Koreksi |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T-s01 | net-01 | TF-1 · D1 · 2 | `b` / `c` | A | M | M | A | A+M | A | A | M | A | A | F-34 |
| T-s02 | net-01 | TF-2 · D2 · 3 | `a,c,d` / `b,c,e` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s03 | net-01 | TF-1 · D1 · 2 | `a` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s04 | ip-01 | TF-1 · D1 · 2 | `c` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s05 | ip-01 | TF-3 · D1 · 2 | `255` / `4,4 oktet,4oktet` | A | M | M | A+S | — | A | A | M | A | A | F-42 |
| T-s06 | ip-01 | TF-2 · D2 · 3 | `a,b,d` / `b,c,e` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s07 | ip-01 | TF-1 · D3 · 4 | `a` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s08 | subnet-01 | TF-3 · D1 · 2 | `254,254 alamat,254alamat` / `256,256 alamat,256alamat` | A | M | M | A+S | — | A | A | M | A | A | F-42 |
| T-s09 | subnet-01 | TF-3 · D2 · 3 | `172.19.44.0` / `10.8.250.0` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s10 | subnet-01 | TF-3 · D2 · 3 | `192.168.73.255` / `172.30.2.255` | A | M | M | A+S | — | A | A | M | A | A |  |
| T-s11 | subnet-01 | TF-4 · D3 · 4 | `d` / `c` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s12 | proto-01 | TF-1 · D1 · 2 | `b` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s13 | proto-01 | TF-1 · D2 · 3 | `b` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s14 | proto-01 | TF-1 · D2 · 3 | `d` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s15 | layer-01 | TF-1 · D1 · 2 | `c` / `b` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s16 | layer-01 | TF-4 · D2 · 3 | `c` / `d` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s17 | layer-01 | TF-1 · D3 · 4 | `d` / `a` | A | M | M | A | A+M | A | A | M | A | A |  |
| T-s18 | rate-01 | TF-3 · D1 · 2 | `3,3 MB/s,3MB/s` / `56,56 Mbps,56Mbps` | A | M | M | A+S | — | A | A | M | A | A | F-42 |
| T-s19 | rate-01 | TF-3 · D2 · 3 | `160,160 detik,160detik` / `112,112 detik,112detik` | A | M | M | A+S | — | A | A | M | A | A | F-42 |
| T-s20 | rate-01 | TF-3 · D3 · 4 | `4,4 menit,4menit` / `2,2 menit,2menit` | A | M | M | A+S | — | A | A | M | A | A | F-42 |
| C-s01 | net-01 | CE-S1 · 4 | `b` / `d` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s02 | ip-01 | CE-S2 · 3 | `a,c,e` / `a,c,d` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s03 | subnet-01 | CE-S5 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s04 | proto-01 | CE-S4 · 4 | `YAML` / `YAML` | A | M | M | A+M | M | A | A | M | A | A | F-35 |
| C-s05 | layer-01 | CE-S3 · 4 | `A,B,C,D,E` / `A,B,C,D,E` | A | M | M | A+M | M | A | A | M | A | A |  |
| C-s06 | rate-01 | CE-S2 · 2 | `a,c` / `b,c` | A | M | M | A+M | M | A | A | M | A | A |  |
| L-act-01.vA | ip-01 | 10 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A | F-43 |
| L-act-01.vB | ip-01 | 10 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A | F-43 |
| L-act-02.vA | subnet-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A | F-42, F-46 |
| L-act-02.vB | subnet-01 | 8 pemeriksaan | Σ 40 | A | M | M | A+S | — | A | A | M | A | A | F-42, F-46 |
| L-act-03.vA | net-01, proto-01, layer-01, rate-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A | F-34, F-42 |
| L-act-03.vB | net-01, proto-01, layer-01, rate-01 | 6 pemeriksaan | Σ 30 | A | M | M | A+S | — | A | A | M | A | A | F-34, F-42 |
| P (spec+rubrik) | semua LO | MR-A | contoh 21 | A | M | M | S | — | A+S | A+S | — | A | A | F-28, F-46 |
| les-01 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-62, F-34 |
| les-02 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-49, F-43 |
| les-03 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-35, F-63, F-50 |
| les-04 + latihan | LO | Pelajaran | — | M | M | M | M | — | — | — | — | M | A | F-64, F-51 |
| remedial | semua LO | TPL-14 | — | M | M | M | M | — | — | — | — | M | A | F-67, F-35, F-43 |

CE-S5 (s03) diperiksa: satu baris salah per varian, koreksi tunggal sesuai model W3 (opsi lain tidak setara). CE-S3 (s05): 1 urutan per varian (5 langkah), urutan tampilan bukan urutan jawaban; skor pasangan berurutan dalam satu urutan diterima.

### 11.3 Fixture evaluator baru (dokumentasi, bukan evaluator produksi)

| Fixture | Input | Diharapkan | K1/K2/K3 · total | Alasan |
|---|---|---|---|---|
| E18 | F1 kosong; lainnya acuan | Perangkat K1.c02–c06 tetap dinilai | 42/18/6 · 76 | Dibandingkan dengan `192.168.50.1` yang diwajibkan, bukan F1 (F-28); keunikan dan gateway butuh F1 |
| E19 | F1 `192.168.50.01` (nol di depan) | F1 tidak terbaca | 42/18/6 · 76 | Sama dengan E18 |
| E20 | F1 `192.168.50.1/24` | Terbaca, tidak ketat | 60/20/6 · 96 | `suffix_24_rule` (F-46): kebenaran penuh, format K3.c01 hilang |
| E21 | F1 `192.168.50.300`, D1 `192.168.50.1` | F1 tidak terbaca; D1 bentrok dengan alamat router wajib | 37/18/6 · 71 | c02 gagal walaupun F1 tidak terbaca — tanpa kredit yang tidak didukung |

Contoh rubrik: **21/21** cocok dengan evaluator dokumentasi. Jumlah rencana bernilai penuh tetap **78.485.511.600** (= P(153,5); kontrak koreksi tidak mengubah ruang solusi sah).

### 11.4 Regresi skor dan durasi

W3: teori 56 (D1 16, D2 24, D3 16; TP-B 40/40/20); S = 1.635 → S_buffer 1.799 → timer **32**, review 13, TA-B 48; lab 30 + 40 + 30 = 100; concept 21; proyek 100. Tidak ada perubahan maksimum, durasi, atau XP (305 XP/modul; 915 untuk
W2–W4). Aturan lulus tetap: 4·e ≥ 3·m per komponen (skor terbaik) dan
Σ bobot·e/m ≥ 80% eksak; pembulatan hanya untuk tampilan.

### 11.5 Visibilitas dan keamanan (QC-06, QC-11, VC-1–VC-5)

Pemindai V-L dijalankan ulang: semua temuan termasuk kategori yang sudah
diterima di bagian visibilitas di atas (fakta yang diajarkan dan diuji
sebagai ingatan; data input fixture yang tampil di spesifikasi; positif palsu
substring). Tidak ada judul pembuka jawaban, urutan tampilan CE-S3 = urutan
jawaban, rasional pengecoh sebelum dinilai, atau contoh rubrik yang membuka
jawaban proyek. D-34 dipertahankan (tanpa enkripsi/proteksi kunci palsu).
Semua skenario fiktif dan defensif; tidak ada kredensial nyata, kode
berbahaya, sistem tanpa izin, atau latihan ofensif.

### 11.6 Pedagogi

Penjelasan mendahului penilaian; koreksi putaran ini menambah koreksi
miskonsepsi pada pelajaran yang tersentuh (kolom "Koreksi" di §11.2) tanpa
menambah menit (anggaran 480 menit tetap). Latihan terbimbing berbeda dari
butir bernilai (dicek silang). Tidak ada ketergantungan pada W5–W16. Tidak
diklaim setara universitas atau efektivitas belajar tervalidasi.

### 11.7 Regresi F-01–F-27

F-01–F-23 (kebenaran rubrik dan kredit independen, distribusi kunci,
kesetaraan varian, enumerasi solusi sah, asumsi akademik, field kanonik,
maksimum tercapai, normalisasi, visibilitas, satuan desimal/biner, kualitas
bukti): diperiksa ulang lewat pemeriksa struktur, simulasi, dan pemindai yang
sama — lolos. F-24–F-27 (pengerasan alur kerja) dipertahankan: tidak ada
perubahan pada `.claude/`, izin, hooks, allowed-tools, asal skill, atau
kontrak alur kerja. V03 tetap verifikasi sesi baru yang dilaporkan
sebelumnya; **tidak** dijalankan ulang di putaran ini.

### 11.8 Batas dan metrik putaran koreksi

*Historis (putaran 1):* temuan F-55, F-56, F-57, F-59 saat itu **BLOCKED** — penutupan penuh register tidak
diklaim. Metrik (perkiraan dari transkrip, ±10%): satu putaran koreksi untuk
W2–W4 bersama; aksi gagal yang tercatat: patch multi-pasangan yang gagal
total (dijalankan ulang per pasangan) dan beberapa total fixture hitungan
tangan yang salah (dikoreksi dari evaluator dokumentasi); pemulihan sesi 1
(konteks diringkas). TOKEN USAGE: **NOT MEASURABLE**.

## 12. Koreksi terarah putaran 2 (delta review PR #27; 2026-11-24)

Delta review independen = **REQUEST CHANGES**. Sebelum mengedit
diverifikasi: PR #27 terbuka, belum di-merge; head
`145bb5693320c322eda4d7ea0d08b0a284018c9e`, base
`ab0103e4954ead4ded6343d105d73a2729916cd6`, branch `planning/cb1-w02-w04`.
Register di §11.1 kini memuat **45 ID** (F-28–F-72) dengan satu disposisi
per ID; deskripsi F-55, F-56, F-57, F-59 dipulihkan owner, sehingga tidak
ada lagi yang BLOCKED karena rincian hilang. F-49–F-51 mengikuti deskripsi
asli; koreksi putaran 1 yang tercatat di bawah ID itu dipertahankan.

### 12.1 Perubahan dan bukti modul ini

| ID | Perubahan putaran 2 | Bukti terjalankan |
|---|---|---|
| F-49 | `theory/items/s07.yaml` vA opsi a + pembahasan (privat tidak dirutekan langsung; CGNAT); vB pembahasan "skenario tanpa CGNAT"; `lessons/les-02.md` NAT/CGNAT | Kunci tetap a / c (`validate.py`) |
| F-50 | `theory/items/s13.yaml` vA: asumsi skenario (halaman sama tanpa peringatan sertifikat; pesan nama tidak ditemukan), rasional c, pembahasan "dugaan terkuat, bukan bukti pasti" | Kunci tetap b |
| F-51 | `theory/items/s18.yaml` (`normalization` peka huruf untuk satuan + `normalization_examples`), `lab/act-03/checks.yaml` (c05 peka huruf; contoh vA/vB), `lab/act-03/spec.md`, `lessons/les-04.md` | `norm_check.py`: 8/8 fixture owner sesuai (3 MB/s, 3MB/s, 3 → benar; 3 Mb/s → salah; 56 Mbps, 56Mbps, 56 → benar; 56 MBps → salah); 107 contoh normalisasi W2–W4 lolos; setiap butir dengan satuan MB/s atau Mbps memakai aturan peka huruf. Head lama: act-03 vA c05 menerima `12 mb/s` dan `12 Mb/s` (cacat terkonfirmasi) |
| F-31 | Tidak ada perubahan | Commit produksi `9a562ce` dan head: TF-3 = 7 slot di blueprint dan "TF-3 × 7" di review |

Satuan kecepatan yang diterima persis: `MB/s` (soal yang meminta MB/s) dan
`Mbps` (soal yang meminta Mbps), dengan atau tanpa satu spasi, atau angka
saja. Satuan `detik`/`menit` dan kode/kata biasa tetap tidak peka huruf.

### 12.2 Prosedur validasi (skrip dokumentasi sementara di scratchpad sesi, tidak di-commit)

| Prosedur | Hasil teramati |
|---|---|
| `validate.py mod-w01` … `mod-w04` (struktur, ID unik, kunci di opsi, poin, durasi A.4, field kanonik) | NO ERRORS × 4 |
| `sim_w02.py`, `sim_w03.py`, `sim_w04.py` (evaluator dokumentasi; dihitung ulang tanpa memakai total yang dinyatakan) | W2 22/22 + F-71 OK; W3 21/21; W4 20/20 + 34 asersi dependensi |
| `norm_check.py` (F-51 dan seluruh `normalization_examples`) | 8/8 fixture owner; 107 contoh; ALL OK |
| `scan_vl.py` (V-L) | Hit W2 3 · W3 23 · W4 12 — sama dengan putaran 1, semua kategori yang sudah diterima |
| Inspeksi dokumen | Pembacaan manual penyusun untuk butir yang diubah (bukan review independen) |

Baseline tetap (diverifikasi dari isi): teori 56/56/56; lab 100/100/100;
proyek 100/100/100; concept 20/21/20; timer 33/32/32 menit; TP-B 8/8/4
slot; XP 305 per modul (915); 480 menit per modul; bobot 30/40/20/10, lulus
≥ 75 per komponen dan ≥ 80 berbobot (eksak). Tidak ada runtime yang
diverifikasi; tidak ada evaluator produksi.

### 12.3 Regresi F-01–F-27

Pemeriksa yang sama dengan putaran 1 lolos (kunci, kesetaraan varian,
maksimum, normalisasi, visibilitas, satuan desimal/biner, enumerasi solusi:
W2 1, W3 78.485.511.600, W4 163.840 — tidak berubah). F-24–F-27
dipertahankan: tidak ada perubahan `.claude/`, izin, hooks, allowed-tools,
asal skill, atau kontrak alur kerja; W1 tidak diubah. V03 tidak dijalankan
ulang. TOKEN USAGE: **NOT MEASURABLE**.
