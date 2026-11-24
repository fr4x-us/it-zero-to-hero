# IT ZERO → HERO — Decision Sheet OD-2: Pemalsuan Backup dan Integritas Akademik

Status: **DIPUTUSKAN OWNER — D-17 (2026-11-24)**, lihat §8 · dokumentasi saja · tanpa kode.
Tanggal: **2026-11-24**. Basis: `main` = `b789e9a` (merge PR #21).

Rekomendasi di §6 adalah saran, **bukan** keputusan. Keputusan restore
yang sudah disetujui (D-03) tidak diubah.

## 1. Empat sifat yang harus dibedakan

| Sifat | Arti | Apakah backup terenkripsi kata sandi (OD-1) memberikannya? |
|---|---|---|
| **Kerahasiaan** | Isi backup tidak terbaca tanpa kata sandi | Ya, terhadap pihak tanpa kata sandi |
| **Integritas kriptografis** | Perubahan isi terdeteksi | Ya, terhadap pihak tanpa kata sandi (tag AEAD) |
| **Autentisitas** | File benar-benar dibuat oleh aplikasi yang sah | **Tidak.** Siapa pun yang tahu kata sandi dapat membuat file valid; kunci tersembunyi di APK dapat diekstrak |
| **Kepercayaan akademik** | Nilai mencerminkan kerja dan kompetensi nyata siswa | **Tidak.** Tidak ada mekanisme teknis — dengan atau tanpa server — yang dapat sepenuhnya membuktikannya (mis. bantuan orang lain saat mengerjakan) |

**Pernyataan tegas:** enkripsi terautentikasi berbasis kata sandi **tidak**
mencegah pemalsuan nilai yang disengaja oleh orang yang mengetahui kata
sandi backup (BKP:T-03).

## 2. Keputusan yang sudah ada (dipertahankan)

| ID | Isi | Sumber |
|---|---|---|
| I-B1 | BKP:M-2 default: restore ditolak bila akan menghilangkan attempt yang ada di data aktif tetapi tidak ada di backup | D-03 |
| I-B2 | BKP:M-1 hanya lewat konfirmasi eksplisit dan snapshot pra-restore yang dapat dipulihkan | D-03 |
| I-B3 | Tanpa penggabungan riwayat nilai otomatis | D-01 M-16, D-03 |
| I-B4 | Auto Backup Android dinonaktifkan | D-07 |
| I-B5 | XP terpisah dari nilai; XP sekali per identitas aktivitas | BL:35, BL:49, TD:22 |

## 3. Ancaman

| ID | Ancaman | Dapat dideteksi/dicegah? |
|---|---|---|
| IT-1 | Kerusakan tidak sengaja (file rusak, terpotong) | **Terdeteksi** (tag AEAD, validasi panjang) |
| IT-2 | Modifikasi oleh pihak tanpa kata sandi | **Terdeteksi** (tag AEAD) |
| IT-3 | Manipulasi nilai sengaja oleh pemilik kata sandi | **Tidak dapat dicegah** oleh kripto offline |
| IT-4 | Attempt akademik palsu disisipkan | Sama dengan IT-3 |
| IT-5 | XP dan achievement diubah | Sama dengan IT-3 |
| IT-6 | Replay backup lama yang valid | Default BKP:M-2 menolak bila attempt aktif akan hilang; BKP:M-1 mengizinkan penggantian eksplisit (snapshot tetap ada) |
| IT-7 | Perangkat di-root / terkompromi | Database aktif dapat diubah langsung tanpa backup; di luar kendali aplikasi |
| IT-8 | Restore lintas perangkat | Didukung oleh desain portabel (kata sandi); tidak dapat membuktikan asal perangkat |

Risiko yang perlu dicatat: BKP:M-1 memungkinkan pengguna mengganti data
aktif dengan backup lama yang tidak memuat attempt gagal terbaru. Riwayat
itu tetap ada di snapshot pra-restore, tetapi tidak lagi di data aktif.

## 4. Pendekatan

| Opsi | Isi | Kelebihan | Kekurangan |
|---|---|---|---|
| I-1 Terima risiko residual + transparansi | Model ancaman: lindungi dari kerusakan dan pihak ketiga; catat asal-usul data (penanda "dipulihkan dari backup tanggal X") dan log peristiwa restore | Sederhana; jujur; portabel | Tidak mencegah pemalsuan oleh pemilik kata sandi |
| I-2 Tanda tangan kunci terikat perangkat (Android Keystore, kunci *non-exportable*, OD1:C5) | Backup ditandatangani kunci perangkat; perangkat yang sama dapat memverifikasi | Mendeteksi file buatan luar aplikasi di perangkat yang sama | Merusak portabilitas: perangkat lain tidak dapat memverifikasi; kehilangan perangkat = tanda tangan tak terverifikasi; perangkat di-root tetap dapat memakai kunci lewat proses aplikasi (NOT VERIFIED) |
| I-3 Rantai hash riwayat attempt (*tamper-evident ledger*) di database | Setiap attempt menyimpan hash attempt sebelumnya | Mendeteksi edit kasual yang tidak menghitung ulang rantai | Algoritma ada di APK, sehingga pemalsu dapat menghitung ulang rantai; bukan pencegahan |
| I-4 Validasi/atestasi sisi server | Rekaman atau validasi di server | Dapat **memperkuat** provenance dan integritas data (mis. waktu pengerjaan tercatat di luar perangkat) | Tetap **tidak dapat secara mandiri membuktikan kompetensi siswa yang sebenarnya**; bertentangan dengan offline-first dan tidak ada server dalam blueprint — **di luar cakupan** |

## 5. Model ancaman yang diusulkan (PROPOSED)

- **Dilindungi:** kerahasiaan backup dan integritas kriptografis terhadap
  pihak tanpa kata sandi (IT-1, IT-2); kehilangan riwayat tanpa jejak
  (I-B1, I-B2).
- **Tidak dilindungi (risiko residual yang diterima secara eksplisit):**
  pemalsuan oleh pemilik kata sandi (IT-3–IT-5), manipulasi pada perangkat
  di-root (IT-7), dan klaim kepercayaan akademik di luar aplikasi.
- **Transparansi:** data hasil restore diberi penanda asal-usul, dan
  setiap restore dicatat di log riwayat yang tidak dihapus oleh restore
  berikutnya (perlu diselaraskan dengan BKP:M-1; detail OPEN). Penanda dan
  log ini bersifat **informatif**, bukan bukti yang tahan manipulasi:
  keduanya tersimpan secara lokal dan dapat diubah oleh pemilik perangkat
  atau pemilik kata sandi backup.
- **Pernyataan produk:** rapor dan sertifikat (bila ada) disebut sebagai
  catatan belajar mandiri, bukan bukti akademik tersertifikasi.

## 6. Rekomendasi (saran, bukan keputusan)

**I-1** untuk V1, dengan penanda asal-usul restore dan log restore yang
bersifat informatif (bukan bukti tahan manipulasi). **I-2**
tidak direkomendasikan untuk V1 karena merusak restore lintas perangkat
(D-01 M-16 "portabel"). **I-3** opsional sebagai pencegah kasual saja dan
tidak boleh diklaim sebagai keamanan.

Risiko residual yang tetap ada: IT-3, IT-4, IT-5, IT-7, serta penggantian
data aktif lewat BKP:M-1 (riwayat hanya di snapshot).

## 7. Pertanyaan untuk owner — *historis, dijawab D-17*

1. **OD-2-Q1:** Terima model ancaman §5, termasuk risiko residual bahwa pemilik kata sandi dapat memalsukan nilai, attempt, dan XP?
2. **OD-2-Q2:** Setujui penanda asal-usul pada data hasil restore dan log restore yang tetap tersimpan, dengan pemahaman bahwa keduanya informatif dan tidak tahan manipulasi?
3. **OD-2-Q3:** Tolak I-2 (tanda tangan terikat perangkat) untuk V1 demi portabilitas?
4. **OD-2-Q4:** I-3 (rantai hash) dimasukkan sebagai pencegah kasual, atau tidak?
5. **OD-2-Q5:** Setujui pernyataan produk bahwa rapor adalah catatan belajar mandiri, bukan bukti akademik tersertifikasi?

~~Status: AWAITING OWNER. OD-2 (UW-16) tetap BLOCKED.~~ *(Historis — dijawab D-17 pada 2026-11-24; lihat §8.)*

## 8. Keputusan owner — D-17 (2026-11-24)

| Butir | Keputusan |
|---|---|
| OD-2-Q1 | I-1 diadopsi; risiko residual terdokumentasi (IT-3–IT-5, IT-7, penggantian data aktif lewat BKP:M-1) diterima secara eksplisit |
| OD-2-Q2 | Penanda asal-usul restore dan log peristiwa restore yang persisten disertakan; keduanya **informatif, tidak tahan manipulasi** |
| OD-2-Q3 | Tanpa tanda tangan terikat perangkat (I-2) di V1 |
| OD-2-Q4 | Tanpa rantai hash riwayat attempt (I-3) di V1 |
| OD-2-Q5 | Rapor akademik adalah catatan belajar mandiri, bukan bukti akademik tersertifikasi |

Tetap berlaku: enkripsi berbasis kata sandi tidak mencegah pemalsuan oleh
pemilik kata sandi; portabilitas lintas perangkat dipertahankan; D-03
(BKP:M-2 default, BKP:M-1 eksplisit dengan snapshot pra-restore, tanpa
merge riwayat otomatis). OPEN: retensi dan penyimpanan log restore (UW-33).
