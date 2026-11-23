# IT ZERO → HERO — Spesifikasi State Machine Penilaian dan Persistensi

Status: PERSIAPAN · spesifikasi dan acceptance criteria saja · tanpa kode.
Tanggal: 2026-11-23.

Dokumen ini menjabarkan langkah 3 urutan persiapan Batch 02 (TD:62):
*assessment state-machine and persistence acceptance criteria, including
timer/process death and unrounded pass rules*. Dokumen ini tidak mengubah
[`BLUEPRINT_LOCKED.md`](BLUEPRINT_LOCKED.md) dan tidak menetapkan aturan baru.

## 0. Label status dan sumber

| Label | Arti |
|---|---|
| **APPROVED** | Didukung blueprint (`BL:n`) atau keputusan Batch 02 (`TD:n`). |
| **RECOVERED** | Dari [`PLANNING_COMPLETION_BATCH.md`](../PLANNING_COMPLETION_BATCH.md) (`B01 M-xx`). Dipakai sebagai konteks perencanaan, tetapi status persetujuan dokumen itu masih menunggu konfirmasi owner (blocker B-3). |
| **PROPOSED** | Usulan desain dokumen ini. Bukan keputusan; perlu persetujuan owner. |
| **OPEN** | Belum diputuskan. Tidak boleh diisi saat implementasi tanpa keputusan owner. |

Rujukan lain: [`QUALITY_GATES.md`](QUALITY_GATES.md) (GR-1–GR-10,
OF-4–OF-6), [`PLANNING_HISTORY.md`](PLANNING_HISTORY.md) (L-xx, O-xx, M-xx),
[`TECHNICAL_DECISIONS_BATCH_02.md`](TECHNICAL_DECISIONS_BATCH_02.md).

## 1. Aturan dasar yang sudah disetujui

| ID | Aturan | Status | Sumber |
|---|---|---|---|
| A-01 | Empat komponen: Theory 30%, Laboratory 40%, Mini-project 20%, Concept explanation 10%. | APPROVED | BL:27–30, TD:31 |
| A-02 | Lulus bila skor akhir berbobot ≥ 80 **dan** setiap komponen ≥ 75. | APPROVED | BL:31–32, TD:30 |
| A-03 | Ambang lulus dihitung dari skor **tanpa pembulatan**; pembulatan hanya untuk tampilan. | APPROVED | TD:21, TD:30 |
| A-04 | Remedial tanpa batas. | APPROVED | BL:33 |
| A-05 | Skor terbaik setiap komponen dipertahankan; seluruh catatan percobaan disimpan. | APPROVED | BL:34, TD:32 |
| A-06 | Ujian teori berwaktu dengan tenggat persisten. | APPROVED | BL:36 |
| A-07 | Sesi lab dan proyek fleksibel. | APPROVED | BL:37 |
| A-08 | Penilaian objektif, offline, tanpa AI. | APPROVED | BL:38, TD:33 |
| A-09 | XP terpisah dari nilai akademik; tanpa penalti XP dan tanpa XP farming. | APPROVED | BL:35, BL:49, TD:37 |
| A-10 | XP diberikan sekali per identitas aktivitas yang sama; pengulangan/remedial tidak memberi XP itu lagi; ledger award persisten. | APPROVED (arah) | TD:22, TD:38 |
| A-11 | Modul dibuka secara linear. | APPROVED | BL:21 |
| A-12 | Durasi ujian diturunkan dari jumlah, tipe, dan kompleksitas soal; tenggat dan jawaban autosave dipersisten; timer berjalan saat aplikasi tertutup; membuka kembali setelah tenggat menilai jawaban yang sudah tersimpan. | RECOVERED | B01 M-07 |
| A-13 | Lab dan mini-project tidak berwaktu; dapat dijeda dan dilanjutkan. | RECOVERED | B01 M-08 |
| A-14 | Penjelasan konsep memakai tugas terstruktur yang dapat diperiksa objektif secara offline, bukan esai bebas atau skor AI. | RECOVERED | B01 M-06 |
| A-15 | Jangan menyimpulkan agregasi antarmodul tanpa aturan terpisah yang disetujui. | APPROVED | TD:32 |

## 2. Model state

Ada dua lapis state (PROPOSED):

1. **Attempt** — satu percobaan pada satu komponen penilaian.
2. **Status komponen dan unit penilaian** — ringkasan dari semua attempt.

Cakupan "unit penilaian" (per modul, per fase, atau keseluruhan program)
adalah **OPEN** (O-03, A-15). Spesifikasi ini tidak memilihnya.

### 2.1 State attempt (PROPOSED)

| State | Nama Indonesia | Arti |
|---|---|---|
| `NOT_STARTED` | Belum mulai | Attempt belum dibuat; belum ada catatan. |
| `IN_PROGRESS` | Berlangsung | Attempt aktif; jawaban/kode dapat diubah. |
| `SAVED` | Tersimpan | Lab/proyek/penjelasan konsep dijeda; seluruh pekerjaan tersimpan. **Tidak berlaku untuk ujian teori** (timer tidak berhenti, A-12). |
| `SUBMITTED` | Selesai | Attempt dikunci; tidak ada perubahan jawaban. |
| `GRADED` | Dinilai | Skor objektif tersimpan permanen pada attempt. |

Hasil attempt (`GRADED`) tidak pernah diubah atau dihapus (A-05).

### 2.2 Status komponen (PROPOSED)

| Status | Nama Indonesia | Kondisi |
|---|---|---|
| `NO_ATTEMPT` | Belum mulai | Tidak ada attempt `GRADED`. |
| `BELOW_THRESHOLD` | Gagal (sementara) | Skor terbaik < 75. Bukan status akhir: remedial selalu tersedia (A-04). |
| `MEETS_THRESHOLD` | Memenuhi ambang | Skor terbaik ≥ 75. |

### 2.3 Status unit penilaian (PROPOSED)

| Status | Nama Indonesia | Kondisi |
|---|---|---|
| `INCOMPLETE` | Belum lengkap | Ada komponen tanpa attempt `GRADED`. |
| `NOT_PASSED` | Belum lulus — remedial | Semua komponen dinilai, tetapi A-02 belum terpenuhi. |
| `PASSED` | Lulus | A-02 terpenuhi. |

"Gagal" dan "remedial" bukan state terminal: status `NOT_PASSED` selalu
memungkinkan attempt baru (A-04).

**OPEN:** apakah keputusan lulus memakai skor **terbaik** per komponen
(tafsiran paling langsung atas A-05 dan B01 M-05), dan apakah `PASSED`
dapat berubah bila konten direvisi (TD:39). Spesifikasi ini mencontohkan
perhitungan dengan skor terbaik, tetapi menandainya **OPEN-CONFIRM**.

## 3. Tabel transisi attempt

### 3.1 Ujian teori (berwaktu)

| # | Dari | Peristiwa | Ke | Efek wajib | Status |
|---|---|---|---|---|---|
| T1 | `NOT_STARTED` | Pengguna menekan "Mulai" | `IN_PROGRESS` | Simpan attempt, `startedAt`, dan **tenggat absolut** dalam satu transaksi **sebelum** soal pertama tampil. | PROPOSED (dasar A-06, A-12) |
| T2 | `IN_PROGRESS` | Jawaban berubah | `IN_PROGRESS` | Autosave jawaban. | APPROVED/RECOVERED (BL:60, A-12) |
| T3 | `IN_PROGRESS` | Aplikasi ditutup / process death / restart | `IN_PROGRESS` | Tidak ada; timer tetap berjalan. | RECOVERED (A-12) |
| T4 | `IN_PROGRESS` | Dibuka kembali sebelum tenggat | `IN_PROGRESS` | Pulihkan jawaban dan sisa waktu dari tenggat tersimpan. | RECOVERED (A-12) |
| T5 | `IN_PROGRESS` | Pengguna menekan "Kumpulkan" sebelum tenggat | `SUBMITTED` | Kunci attempt; simpan `submittedAt`. | PROPOSED |
| T6 | `IN_PROGRESS` | Tenggat tercapai saat aplikasi terbuka | `SUBMITTED` | Kunci; hanya jawaban yang tersimpan sebelum tenggat yang dipakai. | PROPOSED (dasar A-12) |
| T7 | `IN_PROGRESS` | Dibuka kembali **setelah** tenggat | `SUBMITTED` → `GRADED` | Nilai jawaban yang sudah tersimpan. | RECOVERED (A-12) |
| T8 | `SUBMITTED` | Penilai objektif selesai | `GRADED` | Simpan skor tanpa pembulatan; perbarui status komponen; proses XP (§7). | PROPOSED (dasar A-03, A-08) |

Ujian teori tidak memiliki state `SAVED` (tidak ada jeda).

### 3.2 Lab, mini-project, penjelasan konsep (tidak berwaktu)

| # | Dari | Peristiwa | Ke | Efek wajib | Status |
|---|---|---|---|---|---|
| L1 | `NOT_STARTED` | Mulai | `IN_PROGRESS` | Simpan attempt. | PROPOSED |
| L2 | `IN_PROGRESS` | Perubahan kode/jawaban | `IN_PROGRESS` | Autosave. | APPROVED (BL:60) |
| L3 | `IN_PROGRESS` | Jeda / keluar / process death | `SAVED` | Semua pekerjaan sudah tersimpan. | RECOVERED (A-13) |
| L4 | `SAVED` | Lanjutkan | `IN_PROGRESS` | Pulihkan seluruh pekerjaan. | RECOVERED (A-13) |
| L5 | `IN_PROGRESS` | Kumpulkan | `SUBMITTED` | Kunci attempt. | PROPOSED; aturan pengumpulan rinci **OPEN** (B01 M-08) |
| L6 | `SUBMITTED` | Test case objektif selesai | `GRADED` | Simpan skor tanpa pembulatan; status komponen; XP. | PROPOSED (dasar A-08, LB-5) |

### 3.3 Transisi status komponen dan unit

| # | Kondisi | Hasil | Status |
|---|---|---|---|
| C1 | Attempt `GRADED` baru dengan skor > skor terbaik | Skor terbaik diperbarui; attempt lama tetap tersimpan. | APPROVED (A-05) |
| C2 | Attempt `GRADED` baru dengan skor ≤ skor terbaik | Skor terbaik tetap; attempt baru tersimpan. | APPROVED (A-05) |
| C3 | Skor terbaik komponen ≥ 75 | `MEETS_THRESHOLD` | APPROVED (A-02) |
| C4 | Semua komponen dinilai, A-02 tidak terpenuhi | `NOT_PASSED`; remedial tersedia untuk komponen mana pun | APPROVED (A-02, A-04); komponen yang boleh diulang **OPEN** |
| C5 | A-02 terpenuhi | `PASSED` | APPROVED (A-02); basis skor OPEN-CONFIRM |
| C6 | `PASSED` | Modul berikutnya terbuka | APPROVED arah (A-11); aturan rinci **OPEN** (B01 M-04) |

Attempt baru (remedial) dimulai dari `NOT_STARTED` sebagai catatan
terpisah. Tidak ada transisi yang menghapus atau menimpa attempt lama.

## 4. Persistensi (PROPOSED kecuali disebut lain)

| ID | Aturan |
|---|---|
| P-01 | Room/SQLite adalah sumber kebenaran state penilaian (BL:11); UI membaca state dari repository, bukan sebaliknya. |
| P-02 | Setiap transisi §3 ditulis secara transaksional; tidak ada state yang hanya ada di memori. |
| P-03 | Autosave pada setiap perubahan jawaban/kode yang berarti (BL:60, OF-4). Interval atau debounce: **OPEN**, tetapi tidak boleh membuat kehilangan pekerjaan yang sudah terlihat oleh pengguna setelah process death. |
| P-04 | Rotasi layar dan perubahan konfigurasi tidak mengubah state attempt maupun sisa waktu. |
| P-05 | Process death dan force stop: saat dibuka kembali, attempt `IN_PROGRESS`/`SAVED` dipulihkan dari database (OF-5). |
| P-06 | Restart perangkat: sama dengan P-05; ujian teori menghitung ulang sisa waktu dari tenggat tersimpan (§5). |
| P-07 | Attempt bersifat *append-only*: tidak ada update yang menghapus skor attempt `GRADED`. |
| P-08 | Skor terbaik dapat diturunkan dari daftar attempt; bila disimpan terpisah, harus konsisten dengan attempt (diperiksa test). |
| P-09 | Migrasi skema Room mempertahankan seluruh attempt dan ledger XP (OF-6). |
| P-10 | Restore backup mempertahankan riwayat attempt (BL:63–64, L-83); penggabungan riwayat nilai otomatis tidak dilakukan (B01 M-16). |

## 5. Tenggat ujian teori yang persisten

### 5.1 Acceptance criteria

| ID | Kriteria | Status |
|---|---|---|
| D-01 | Tenggat disimpan sebagai **waktu absolut** saat attempt dimulai, sebelum soal tampil. | PROPOSED (dasar A-12) |
| D-02 | Timer terus berjalan saat aplikasi ditutup, process death, dan restart perangkat. | RECOVERED (A-12) |
| D-03 | Sisa waktu selalu dihitung dari tenggat tersimpan, tidak dari timer di memori. | PROPOSED |
| D-04 | Jawaban yang tersimpan sebelum tenggat dinilai; perubahan setelah tenggat ditolak. | RECOVERED (A-12) |
| D-05 | Membuka aplikasi setelah tenggat langsung mengunci dan menilai jawaban tersimpan (T7). | RECOVERED (A-12) |
| D-06 | Remedial membuat attempt baru dengan tenggat baru; tenggat attempt lama tidak berubah. | PROPOSED (dasar A-04) |
| D-07 | Tenggat disimpan sebagai *instant* (UTC); tampilan memakai Asia/Tokyo (BL:52). | PROPOSED |
| D-08 | Durasi ujian dihitung dari jumlah, tipe, dan kompleksitas soal; rumusnya **OPEN**. | RECOVERED arah, rumus OPEN |

### 5.2 Risiko jam perangkat dan kasus tepi

Blueprint tidak mengatur manipulasi jam; aturan di bawah adalah **analisis
risiko dan usulan deteksi**, bukan perubahan aturan.

| # | Kasus | Risiko | Usulan (PROPOSED) | Kebijakan |
|---|---|---|---|---|
| E-01 | Pengguna memundurkan jam perangkat | Waktu ujian bertambah | Simpan juga jam monotonic sejak boot (`elapsedRealtime`) saat mulai; selama tidak reboot, hitung sisa waktu dari jam monotonic. | Penanganan bila terdeteksi: **OPEN** |
| E-02 | Pengguna memajukan jam perangkat | Ujian berakhir lebih cepat | Sama dengan E-01. | **OPEN** |
| E-03 | Reboot saat ujian | Jam monotonic ter-reset | Pakai jam dinding; catat bahwa jaminan anti-manipulasi melemah. | **OPEN** |
| E-04 | Sinkronisasi jam otomatis (NTP) mengoreksi jam | Lompatan kecil | Toleransi lompatan: **OPEN**. | **OPEN** |
| E-05 | Zona waktu perangkat diubah | Tampilan salah | Instant UTC tidak terpengaruh; tampilan tetap Asia/Tokyo. | PROPOSED |
| E-06 | Tenggat tercapai tepat saat autosave berjalan | Jawaban terakhir hilang atau ikut dinilai setelah tenggat | Penanda waktu simpan dibandingkan dengan tenggat dalam satu transaksi. | PROPOSED |
| E-07 | Baterai habis / crash di tengah ujian | Kehilangan jawaban | Autosave per perubahan (P-03). | APPROVED arah |
| E-08 | Ujian dimulai sebelum 22:00 dan berakhir di jam tenang | Notifikasi pengingat | Jam tenang hanya mengatur notifikasi (BL:57), tidak menghentikan timer. | PROPOSED |

Aplikasi offline tidak dapat menjamin waktu tepercaya. Semua deteksi di
atas hanya mempersulit manipulasi, bukan mencegahnya. Catatan ini tidak
dianggap sebagai jaminan keamanan.

## 6. Rumus skor dan keputusan lulus

### 6.1 Rumus (APPROVED: bobot dan ambang; PROPOSED: notasi)

```
W = 0,30 × T + 0,40 × L + 0,20 × P + 0,10 × C
LULUS ⇔ W ≥ 80  DAN  T ≥ 75  DAN  L ≥ 75  DAN  P ≥ 75  DAN  C ≥ 75
```

T, L, P, C = skor komponen 0–100 (B01 M-05), dihitung tanpa pembulatan (A-03).
Contoh di bawah memakai skor terbaik per komponen (OPEN-CONFIRM, §2.3).

### 6.2 Risiko representasi angka

- Pecahan biner (*floating point*) dapat menghasilkan 79,999… untuk nilai
  yang seharusnya tepat 80. Representasi angka (mis. bilangan bulat
  berskala atau desimal tepat) adalah **OPEN** (TD:21).
- Acceptance: kasus tepat-ambang di §6.3 harus lulus/gagal sesuai
  aritmetika eksak, apa pun representasinya.

### 6.3 Tabel kasus batas

| # | T | L | P | C | W (eksak) | Hasil | Alasan |
|---|---|---|---|---|---|---|---|
| B-01 | 80 | 80 | 80 | 80 | 80,0 | LULUS | Tepat ambang W |
| B-02 | 75 | 75 | 75 | 75 | 75,0 | BELUM LULUS | W < 80 |
| B-03 | 75 | 85 | 80 | 75 | 80,0 | LULUS | W tepat 80 dari pecahan (22,5 + 34 + 16 + 7,5) |
| B-04 | 100 | 100 | 100 | 74 | 97,4 | BELUM LULUS | C < 75 walau W tinggi |
| B-05 | 75 | 75 | 100 | 100 | 82,5 | LULUS | Semua ≥ 75, W ≥ 80 |
| B-06 | 75 | 75 | 75 | 100 | 77,5 | BELUM LULUS | Semua ≥ 75 tetapi W < 80 |
| B-07 | 79,97 | 80 | 80 | 80 | 79,991 | BELUM LULUS | Tampilan bulat "80" tidak boleh meluluskan (A-03) |
| B-08 | 100 | 100 | 100 | 74,999 | 97,4999 | BELUM LULUS | C tampil "75" bila dibulatkan, tetapi < 75 |
| B-09 | 100 | 75 | 75 | 75 | 82,5 | LULUS | Semua tepat 75 kecuali T |
| B-10 | Komponen C belum pernah dinilai | — | — | — | — | BELUM LENGKAP | `INCOMPLETE` |

### 6.4 Remedial dan skor terbaik

| # | Riwayat attempt komponen L | Skor terbaik | Attempt tersimpan | Catatan |
|---|---|---|---|---|
| R-01 | 60 | 60 | 1 | `BELOW_THRESHOLD` |
| R-02 | 60 → 90 | 90 | 2 | Skor terbaik naik |
| R-03 | 60 → 90 → 70 | 90 | 3 | Attempt lebih rendah tidak menurunkan skor terbaik |
| R-04 | 50 attempt berurutan | Maksimum dari 50 | 50 | Tidak ada batas jumlah (A-04); attempt ke-51 tetap diterima |
| R-05 | 74,99 → 75 | 75 | 2 | Menjadi `MEETS_THRESHOLD` |

## 7. XP (ledger sekali per identitas aktivitas)

| ID | Acceptance criteria | Status |
|---|---|---|
| X-01 | XP dicatat di ledger persisten; satu entri award per identitas aktivitas. | APPROVED arah (TD:38) |
| X-02 | Attempt kedua dan seterusnya untuk identitas yang sama (termasuk remedial) tidak menambah XP itu. | APPROVED (TD:22) |
| X-03 | Tidak ada entri XP negatif atau pengurangan XP karena remedial/gagal. | APPROVED (BL:35, TD:22) |
| X-04 | Award idempoten: crash di antara penilaian dan penulisan XP tidak menghasilkan award ganda atau award hilang (penulisan dalam satu transaksi dengan `GRADED` — PROPOSED). | PROPOSED |
| X-05 | XP tidak memengaruhi skor akademik atau keputusan lulus. | APPROVED (BL:49, TD:37) |
| X-06 | Ledger ikut dalam backup/restore dan migrasi tanpa duplikasi. | PROPOSED (dasar P-09, P-10) |
| X-07 | Definisi identitas aktivitas, jumlah XP, batas, level, streak, achievement, mastery, dan perlakuan konten yang direvisi. | **OPEN** (TD:22, TD:39) |

Contoh (identitas aktivitas masih OPEN; label "kuis-W9-1" hanya ilustrasi):

| # | Peristiwa | XP baru | Alasan |
|---|---|---|---|
| XP-1 | Kuis-W9-1 attempt 1 memenuhi syarat award | Ya (jumlah OPEN) | Award pertama |
| XP-2 | Kuis-W9-1 attempt 2 (remedial) | Tidak | Identitas sama |
| XP-3 | Kuis-W9-1 attempt 1 gagal | Tidak dikurangi | Tanpa penalti |
| XP-4 | App crash setelah `GRADED`, sebelum UI menampilkan XP | Tepat satu award di ledger | Idempoten |

## 8. Contoh skenario pengujian (Given–When–Then, bukan test executable)

| ID | Given | When | Then | Gate |
|---|---|---|---|---|
| S-01 | Ujian teori dimulai, tenggat 30 menit tersimpan | Rotasi layar 5 kali | Jawaban dan sisa waktu tidak berubah | GR-5 |
| S-02 | Ujian teori berjalan, 3 jawaban terisi | Process death, dibuka 5 menit kemudian | 3 jawaban kembali; sisa waktu berkurang 5 menit | GR-5, OF-5 |
| S-03 | Ujian teori berjalan | Aplikasi ditutup, dibuka setelah tenggat | Attempt `GRADED` dengan jawaban tersimpan saja | GR-5 |
| S-04 | Ujian teori berjalan | Jam perangkat dimundurkan 1 jam (tanpa reboot) | Sisa waktu tidak bertambah | GR-5 (E-01) |
| S-05 | Lab `IN_PROGRESS` dengan kode belum dikumpulkan | Force stop, dibuka besok | Kode utuh; state `SAVED` → lanjut `IN_PROGRESS` | OF-4, OF-5 |
| S-06 | Skor terbaik T, L, P, C = 75, 85, 80, 75 | Hitung status | `PASSED` (W tepat 80) | GR-2 |
| S-07 | Skor 79,97 / 80 / 80 / 80 | Hitung status | `NOT_PASSED`, walau tampilan menunjukkan 80 | GR-2, GR-10 |
| S-08 | L: 60 lalu 90 lalu 70 | Lihat riwayat | 3 attempt tersimpan; skor terbaik 90 | GR-3, GR-4 |
| S-09 | Aktivitas sudah memberi XP | Remedial lulus | Ledger tetap satu award; tidak ada XP negatif | GR-8 |
| S-10 | Database berisi 100 attempt | Migrasi skema | 100 attempt dan ledger utuh | OF-6 |

## 9. Keputusan yang masih OPEN

| ID | Topik | Rujukan |
|---|---|---|
| OP-1 | Agregasi skor antarmodul/fase dan cakupan "unit penilaian" | O-03, TD:21, TD:32, B01 M-05 |
| OP-2 | Basis keputusan lulus: skor terbaik per komponen (OPEN-CONFIRM) | GR-10, B01 M-05 |
| OP-3 | Representasi angka, presisi, aturan seri | TD:21 |
| OP-4 | Rubrik objektif penjelasan konsep dan bank tugas | TD:33, B01 M-06 |
| OP-5 | Rumus durasi ujian dan format soal | B01 M-07 |
| OP-6 | Kebijakan bila manipulasi jam terdeteksi; toleransi koreksi NTP | §5.2 |
| OP-7 | Aturan pengumpulan dan interupsi lab/proyek | B01 M-08 |
| OP-8 | Identitas aktivitas XP, jumlah, batas, level, streak, revisi konten | TD:22, TD:39, B01 M-11 |
| OP-9 | Aturan unlock rinci: partial, remedial, konten pratinjau | BL:21, B01 M-04 |
| OP-10 | Komponen mana yang boleh diulang saat `NOT_PASSED` | A-04 |
| OP-11 | Interval/debounce autosave | P-03 |
| OP-12 | Status persetujuan `PLANNING_COMPLETION_BATCH.md` (sumber RECOVERED) | B-3 |

## 10. Keputusan owner D-04 (2026-11-23)

Dicatat dari [OWNER_DECISION_CHECKLIST.md](OWNER_DECISION_CHECKLIST.md).

| Butir | Keputusan | Dampak pada spesifikasi ini |
|---|---|---|
| Basis kelulusan | Skor **terbaik** per komponen; setiap attempt disimpan | OP-2 / OPEN-CONFIRM §2.3 **diputuskan**: contoh §6 dengan skor terbaik berlaku |
| Unit kelulusan | **Per modul**: nilai tertimbang ≥ 80 dan setiap komponen ≥ 75, tanpa pembulatan | OP-1 diputuskan untuk tingkat modul; "unit penilaian" §2.3 = modul |
| Unlock | Modul berikutnya terbuka linear setelah modul sebelumnya lulus | C6 diperjelas; detail pratinjau mengikuti D-01 M-04 (pratinjau boleh, latihan/ujian terkunci, modul lulus tetap dapat diakses) |
| Penyelesaian program | Seluruh 16 modul lulus **dan** capstone selesai menurut rubrik yang akan disetujui | Tidak ada rata-rata program atau ambang tambahan |
| Masih OPEN | Agregasi numerik tingkat program; representasi angka (OP-3); rubrik capstone (CU-9) | — |
| Implikasi untuk dikonfirmasi | Kelulusan per modul dengan empat komponen berarti setiap modul memerlukan Theory, Laboratory, Mini-project, dan Concept explanation | **Tidak** diputuskan di sini; dicatat pada CU-2 |
