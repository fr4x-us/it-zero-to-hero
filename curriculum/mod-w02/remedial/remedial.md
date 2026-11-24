---
module_id: mod-w02
content_version: "1.0"
template: TPL-14
purpose: "Penjelasan ulang dan latihan tambahan per kompetensi untuk persiapan remedial (tidak dinilai)"
---

# Materi Remedial W2

Gunakan bagian yang sesuai dengan kompetensi yang belum dikuasai (umpan
balik ujian menampilkan rincian per kompetensi, FB-A). Latihan di sini tidak
dinilai dan tidak memberi XP. Attempt remedial memakai **varian setara**
yang dipilih bergiliran (VA-2); remedial tidak dibatasi jumlahnya.

## R-OS — Fungsi sistem operasi (LO1)

**Ingat kembali:** sistem operasi = pengelola gedung. Tanyakan: *apakah
yang diatur program yang berjalan?* (proses) · *pembagian RAM?* (memori) ·
*berkas/folder?* (file) · *perangkat lewat driver?* (perangkat) · *cara
pengguna memberi perintah?* (antarmuka).

**Cara lain melihatnya:** aplikasi seperti pelanggan restoran yang memesan
lewat pelayan (OS); pelanggan tidak masuk ke dapur (hardware) sendiri.

**Latihan tambahan:** fungsi OS mana yang paling terlihat — (1) speaker
Bluetooth yang baru dipasangkan langsung mengeluarkan suara; (2) kamu
mengetik perintah teks di jendela Terminal; (3) catatan disimpan sebagai
`ide-lomba.txt`. *Jawaban:* (1) manajemen perangkat; (2) antarmuka
pengguna (CLI); (3) manajemen file.

## R-PROC — Program dan proses (LO2)

**Ingat kembali:** program = resep di buku (berkas di penyimpanan);
proses = kegiatan memasak sekarang (di RAM, punya PID). Mengakhiri proses:
RAM-nya dikembalikan, yang belum disimpan hilang, proses lain tetap
berjalan.

**Latihan tambahan (angka fiktif):** proses "Pengedit audio" (PID 8810,
640 MB, tidak menanggapi) dan "Catatan" (PID 8823, 30 MB, berjalan, ada
tulisan belum disimpan). Apa urutan tindakan yang aman? *Jawaban:* simpan
tulisan di Catatan, lalu akhiri PID 8810; sekitar 640 MB RAM dikembalikan.

## R-FS — Berkas, ekstensi, dan pohon folder (LO3)

**Ingat kembali:** ekstensi = bagian setelah **titik terakhir**; ekstensi
memilih aplikasi pembuka, **tidak** mengubah isi. Nama harus unik di dalam
satu folder.

**Latihan tambahan:** (1) ekstensi `rekap.bulan.juni.xlsx`? (2) jenis
`musik-video.mp3`? (3) Bolehkah `/a/b.txt` dan `/c/b.txt` ada bersamaan?
*Jawaban:* (1) `xlsx`; (2) audio (`mp3`), walaupun namanya memuat "video";
(3) boleh, foldernya berbeda.

## R-PATH — Path absolut dan relatif (LO4)

**Ingat kembali:**

- Absolut: mulai dari root, diawali `/`.
- Relatif: mulai dari folder kerja; **naik** dengan `..` sampai folder yang
  juga leluhur sasaran, lalu **turun**.
- Hitung naik: dari `/x/y/z` ke `/x/w/f.txt`, awalan bersama `/x`; folder
  kerja punya 2 komponen setelah `/x` (`y`, `z`) → naik 2 kali:
  `../../w/f.txt`.

**Latihan tambahan (pohon `/gudang`: `/gudang/rak1/kotak/baut.txt` dan
`/gudang/rak2/obeng.txt`):** (1) path absolut `obeng.txt`; (2) dari
`/gudang/rak1/kotak` ke `obeng.txt`; (3) dari `/gudang/rak1` ke `baut.txt`.
*Jawaban:* (1) `/gudang/rak2/obeng.txt`; (2) `../../rak2/obeng.txt`;
(3) `kotak/baut.txt`.

## R-OPS — Operasi berkas (LO5)

**Ingat kembali:** salin = asal tetap; pindah = asal hilang; hapus = ke
Tempat Sampah; nama sama di tujuan → ditolak (OP-2); telusuri satu langkah
demi satu langkah dengan tabel "isi folder setelah langkah n".

**Latihan tambahan:** awal `/p` berisi `x.txt`, `/q` berisi `x.txt`.
(1) Pindah `/p/x.txt` ke `/q`; (2) salin `/q/x.txt` ke `/p`;
(3) hapus `/q/x.txt`. Berapa berkas di `/p` dan `/q`? *Jawaban:* langkah 1
ditolak; langkah 2 ditolak (nama sama di `/p`); langkah 3 → `/q` kosong.
Hasil `/p` 1, `/q` 0.

## R-PERM — Akun dan izin (LO6)

**Ingat kembali:** baca = lihat; tulis = ubah/simpan/hapus; jalankan =
jalankan program. Hak minimum: beri izin sekecil mungkin yang cukup; pakai
akun biasa sehari-hari.

**Latihan tambahan:** berkas `nilai-akhir.xlsx` milik `walikelas`; akun
`guru-mapel` perlu memasukkan nilai, akun `orang-tua` hanya perlu melihat.
Izin minimum masing-masing? *Jawaban:* `guru-mapel` baca + tulis;
`orang-tua` baca saja.
