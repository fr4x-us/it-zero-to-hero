"""Register kesetaraan akademik 48 slot concept (R4-04/05/06/09) — PENILAIAN PENULIS (semantik), bukan bukti otomatis.
Per slot: (kompetensi bernilai bersama, perilaku bernilai vA, perilaku bernilai vB, perbandingan tuntutan kognitif, status).
Kriteria PASS: kedua varian menuntut jenis penalaran bernilai yang sama — keterampilan yang sama pada konteks berbeda,
atau instans cermin dari aturan yang sama, atau berbagi konsep wajib yang dinilai langsung dengan bobot setara — pada
tingkat tuntutan yang sebanding. OPEN: perilaku bernilai utama adalah sub-keterampilan berbeda atau tingkat tuntutan berbeda.
Rasio jumlah kata hanya penyaring, bukan gerbang."""
P, O = 'PASS', 'OPEN'
N = {
'01': {
 's01': ('Menjelaskan persistensi data dari sifat volatil/non-volatil', 'memilih alasan RAM volatil (isi hilang saat listrik mati)', 'memilih alasan SSD menyimpan data tanpa listrik', 'Instans cermin dari aturan yang sama (volatil vs non-volatil); satu penjelasan sebab-akibat', P),
 's02': ('Menilai manfaat core tambahan dari sifat pekerjaan', 'menilai 4 pernyataan untuk banyak aplikasi bersamaan', 'menilai 4 pernyataan untuk program berurutan', 'Aturan "dapat dibagi" diterapkan pada kasus cermin', P),
 's03': ('Mengurutkan proses boot', 'mengurutkan 5 langkah boot sampai OS siap', 'mengurutkan 5 langkah boot dari flashdisk instalasi', 'Urutan 5 langkah yang sama; konteks bacaan vB lebih panjang tetapi relevan (review independen: PASS)', P),
 's04': ('Memetakan istilah IPOS dan istilah dasar', 'memetakan input, proses, hardware, informasi', 'memetakan output, penyimpanan, software, data', 'Tugas pemetaan identik pada empat istilah dasar berbeda dengan tingkat yang sama', P),
 's05': ('Mendeteksi dan memperbaiki konversi satuan data desimal', 'baris salah 1 GB = 100 MB → 1.000 MB', 'baris salah 500 GB = 50.000 MB → 500.000 MB', 'Kesalahan faktor ×1.000 yang sama; vB satu langkah perkalian lebih', P),
 's06': ('Menilai syarat kompatibilitas rakitan', 'menilai 5 pernyataan soket/RAM/slot/PSU/anggaran', 'menilai 5 pernyataan soket/RAM/slot/PSU/anggaran', 'Konsep dan struktur sama', P)},
'02': {
 's01': ('Memetakan fungsi dan istilah sistem operasi', 'memetakan kernel, memori, perangkat, antarmuka', 'memetakan file, memori, kernel, antarmuka', 'Tugas pemetaan sama; tiga dari empat istilah sama', P),
 's02': ('Menjelaskan akibat mengakhiri proses dari model "proses punya RAM sendiri"', 'memilih alasan tulisan belum disimpan hilang', 'memilih alasan proses lain tetap berjalan', 'Dua akibat cermin dari model yang sama; satu penjelasan', P),
 's03': ('Menafsirkan makna ekstensi berkas', 'menilai pernyataan ganti ekstensi (isi tetap, aplikasi pembuka)', 'menilai pernyataan ekstensi tersembunyi (titik terakhir, isi tetap, exe)', 'Berbagi konsep yang dinilai langsung "isi tidak berubah" di kedua varian; satu konsep berbeda masing-masing dengan bobot setara', P),
 's04': ('Menafsirkan path relatif terpendek', 'baris salah `/Musik` → `../Musik`', 'baris salah `../../sampul.png` → `../sampul.png`', 'Keterampilan sama (menghitung naik tingkat dan membedakan absolut/relatif)', P),
 's05': ('Mengurutkan operasi berkas yang aman', 'pulihkan → periksa seluruh Tempat Sampah → kosongkan (simulasi)', 'salin → verifikasi → hapus → periksa lalu kosongkan (simulasi)', 'Prinsip sama: verifikasi sebelum langkah permanen; 4 langkah, satu urutan', P),
 's06': ('Menerapkan prinsip hak minimum', 'menilai alasan memakai akun biasa', 'menilai izin aplikasi senter dan akun administrator', 'Aturan hak minimum diterapkan pada akun vs izin; keduanya memuat penilaian akun administrator setelah D-39', P)},
'03': {
 's01': ('Menjelaskan batas LAN–internet dan peran perangkat', 'memilih alasan pencetakan LAN tetap jalan tanpa internet', 'memilih alasan router diperlukan untuk ke internet', 'Penalaran batas jaringan yang sama dari dua sisi (lalu lintas lokal vs antarjaringan)', P),
 's02': ('Menilai pernyataan alamat privat/publik', 'menilai 5 pernyataan (rentang privat, unik, NAT)', 'menilai 5 pernyataan (rentang privat, ISP, NAT)', 'Konsep dan struktur sama', P),
 's03': ('Menerapkan aturan subnet /24', 'baris salah: jumlah host 256 → 254 (hitung)', 'baris salah v2.0: jumlah host 2⁸ − 1 = 255 → 254 (hitung)', 'Ronde 6: vB 2.0 kini menilai perhitungan jumlah host yang sama (kurangi alamat jaringan dan broadcast); keanggotaan jaringan pindah ke lab act-02.c06–c08 (vA+vB). Kesetaraan = penilaian penulis; menunggu review independen', P),
 's04': ('Memetakan protokol ke fungsi', 'memetakan DHCP, DNS, HTTPS, UDP', 'memetakan TCP, HTTP, DNS, DHCP', 'Tugas pemetaan sama; dua protokol sama', P),
 's05': ('Mengurutkan pembungkusan TCP/IP', 'mengurutkan 5 langkah mengirim', 'mengurutkan 5 langkah menerima', 'Instans cermin (bungkus vs buka bungkus) dari model lapisan yang sama', P),
 's06': ('Menilai kecepatan bit vs byte dan model ideal', 'menilai 4 pernyataan dari 50 Mbps', 'menilai 4 pernyataan dari 3 MB/s', 'Konversi ×8 dan ideal vs nyata di kedua varian', P)},
'04': {
 's01': ('Mengenali tujuan CIA dan autentikasi', 'memetakan istilah → definisi', 'memetakan kejadian → istilah', 'Konsep sama, tetapi vA pengenalan definisi sedangkan vB klasifikasi skenario; tuntutan kognitif mungkin berbeda (review independen: OPEN)', O),
 's02': ('Mengenali ancaman dan tanda', 'menilai 5 pernyataan (phishing RS, trojan, tanda bukan bukti)', 'menilai 5 pernyataan (phishing RS, trojan, tanda bukan bukti)', 'Konsep yang dinilai sama setelah D-39/R3-06', P),
 's03': ('Mendeteksi kesalahan autentikasi', 'baris salah: hitung kombinasi PIN 3 digit (10³ = 1.000)', 'baris salah v2.0: hitung kombinasi PIN 4 digit (10⁴ = 10.000)', 'Ronde 6: vB 2.0 kini menilai aturan ×10 per digit yang sama; MFA (faktor berbeda jenis) pindah ke lab act-03.c02 (vA+vB). Batas: theory s09 vA juga meminta 10.000 (keterpaparan angka). Penilaian penulis; menunggu review independen', P),
 's04': ('Menilai bukti identitas situs', 'memilih alasan: domain terdaftar + arti HTTPS', 'memilih alasan: arti HTTPS untuk nama domain tertentu', 'Keduanya menuntut membedakan nama domain dari klaim identitas dan arti HTTPS (setelah D-39)', P),
 's05': ('Menilai rencana cadangan dan batas perlindungan', 'menilai pernyataan salinan di laptop yang sama (3-2-1, perlindungan bukan jaminan)', 'menilai alasan cadangan tetap perlu (perlindungan bukan jaminan, pemulihan)', 'Berbagi konsep yang dinilai langsung "perlindungan tidak menjamin" (R3-07); satu konsep berbeda masing-masing', P),
 's06': ('Mengurutkan respons insiden hentikan → amankan', 'mengurutkan 4 langkah ponsel hilang', 'mengurutkan 4 langkah setelah phishing', 'Struktur urutan dan dua urutan diterima sama (review independen: PASS)', P)},
'05': {
 's01': ('Menghitung dengan urutan operasi', 'memetakan 4 ekspresi (kurung, kiri ke kanan)', 'memetakan 4 ekspresi (kurung, pangkat)', 'Keterampilan sama; satu aturan berbeda per varian, pangkat dijamin di teori s06/lab', P),
 's02': ('Menilai pernyataan variabel/ekspresi', 'menilai 5 pernyataan', 'menilai 5 pernyataan', 'Konsep sama (variabel, substitusi, pangkat, rata-rata)', P),
 's03': ('Memeriksa hasil bagi dan sisa', 'baris salah 29 ÷ 4', 'baris salah 38 ÷ 6', 'Keterampilan dan pengecoh (sisa ≥ pembagi) sama', P),
 's04': ('Mengonversi besaran bersatuan campuran', 'jam-menit ke desimal jam', 'kg-g ke gram', 'Keterampilan konversi sama pada satuan berbeda (LO4: waktu dan massa)', P),
 's05': ('Mengurutkan perhitungan persentase dari nilai dasar', 'urutan diskon 25%', 'urutan kenaikan 60 → 75', 'Prosedur nilai dasar sama; dua urutan diterima di kedua varian', P),
 's06': ('Menilai aturan pembulatan', 'menilai 4 pernyataan', 'menilai 4 pernyataan', 'Konsep sama', P)},
'06': {
 's01': ('Membedakan biner, desimal, Boolean', 'memetakan 4 tulisan', 'memetakan 4 tulisan', 'Tugas sama', P),
 's02': ('Mengurutkan konversi biner → desimal', 'prosedur umum 4 langkah', 'memeriksa `1100₂` 4 langkah', 'Prosedur bobot yang sama; vB konkret', P),
 's03': ('Memeriksa biner tepat 8 bit', 'baris salah 37 → 00100101', 'baris salah 52 → 00110100', 'Keterampilan sama', P),
 's04': ('Menjelaskan operator Boolean dari definisinya', 'alasan AND = 0', 'alasan OR = 1', 'Instans cermin dari definisi operator (bandingkan review independen W6 s06: PASS)', P),
 's05': ('Menilai aturan tabel kebenaran', 'menilai 5 pernyataan', 'menilai 5 pernyataan', 'Konsep sama setelah D-39', P),
 's06': ('Menerjemahkan aturan ke BX dan mengenali ekspresi ekuivalen', 'memilih ekspresi "dan"', 'memilih ekspresi "atau"', 'Variasi AND/OR yang wajar (review independen: PASS)', P)},
'07': {
 's01': ('Memilih dekomposisi lengkap tanpa bagian tidak relevan', 'memilih sub-masalah lomba', 'memilih sub-masalah video', 'Tugas sama', P),
 's02': ('Mendeteksi kesalahan pola', 'baris salah: jenis pola 1, 2, 4, 8 (berlipat dikira bertambah tetap)', 'baris salah v2.0: jenis pola 3, 9, 27, 81 (berlipat dikira bertambah tetap)', 'Ronde 6: vB 2.0 kini menilai klasifikasi jenis pola yang sama; rumus suku ke-n pindah ke theory s05 (TF-3, vA+vB). Penilaian penulis; menunggu review independen', P),
 's03': ('Menjelaskan tujuan abstraksi', 'alasan menyaring informasi (peta kereta)', 'alasan v2.0 menyaring informasi menurut tujuan (formulir lomba lari)', 'Ronde 6: vB 2.0 kini menilai penyaringan informasi menurut tujuan, sama dengan vA (CE-S1); generalisasi dengan variabel pindah ke theory s10 (TF-1, vA+vB). Penilaian penulis; menunggu review independen', P),
 's04': ('Menilai kualitas instruksi', 'memetakan 4 instruksi', 'memetakan 4 instruksi', 'Kategori sama', P),
 's05': ('Mengurutkan tugas berprasyarat', '4 tugas, 2 urutan', '4 tugas, 2 urutan', 'Struktur sama', P),
 's06': ('Memilih kasus uji batas', 'aturan ≥ 12', 'aturan ≥ 50.000', 'Struktur sama', P)},
'08': {
 's01': ('Menilai input, output, domain algoritma', 'menilai 5 pernyataan pembagian rata', 'menilai 5 pernyataan konversi detik', 'Konsep sama', P),
 's02': ('Memetakan bentuk flowchart', 'bentuk → kegunaan', 'isi blok → bentuk', 'Arah pemetaan cermin pada tingkat yang sama', P),
 's03': ('Menelusuri percabangan di batas', 'baris salah x = 10 dengan >', 'baris salah x = 5 dengan ≤', 'Keterampilan sama', P),
 's04': ('Menjelaskan berhentinya perulangan', 'alasan tidak berhenti tanpa perubahan', 'alasan perubahan di dalam perulangan', 'Instans cermin dari aturan yang sama', P),
 's05': ('Menyusun tabel penelusuran', '4 baris', '4 baris', 'Struktur sama', P),
 's06': ('Menilai kebenaran algoritma daftar', 'nilai awal, negatif, nilai sama, satu tes', 'nilai awal, daftar kosong, negatif', 'Berbagi konsep yang dinilai langsung (nilai awal, negatif)', P)},
}
