---
activity_id: mod-w03.lab.act-02
component: mod-w03.lab
content_version: "1.0"
variants: [mod-w03.lab.act-02.vA, mod-w03.lab.act-02.vB]
competencies: [comp-w03-subnet-01]
max_points: 40
estimated_minutes: 35
checks_file: checks.yaml
---

# Lab W3 · Aktivitas 2 — Perhitungan Jaringan /24

## Tujuan

1. Menentukan alamat jaringan, broadcast, host pertama, dan host terakhir
   untuk mask `255.255.255.0`.
2. Menghitung alamat host di luar rentang DHCP.
3. Menentukan apakah sebuah alamat dapat dipakai perangkat lain di
   jaringan yang sama.

## Prasyarat

Pelajaran 2 §3–§4, Pelajaran 4 §3.

## Asumsi jaringan (model W3)

Mask selalu `255.255.255.0` (/24). Rentang DHCP ditulis termasuk kedua
ujungnya. "Dapat menjadi alamat perangkat lain di jaringan yang sama"
berarti: valid, berada di jaringan yang sama (tanpa melewati router), dan
bukan alamat jaringan atau broadcast.

**Contoh terlihat (tidak dinilai):** contoh terbimbing Pelajaran 2 §5
(`10.20.30.40`).

## Data (fixture)

| | Varian A | Varian B |
|---|---|---|
| Alamat perangkat | `192.168.20.57` | `10.4.7.130` |
| Mask | `255.255.255.0` | `255.255.255.0` |
| Rentang DHCP router | `192.168.20.60` – `192.168.20.139` | `10.4.7.10` – `10.4.7.59` |

## Pertanyaan

| No. | Varian A | Varian B |
|---|---|---|
| 1 | Alamat jaringan | Alamat jaringan |
| 2 | Alamat broadcast | Alamat broadcast |
| 3 | Host pertama | Host pertama |
| 4 | Host terakhir | Host terakhir |
| 5 | Jumlah alamat host yang **di luar** rentang DHCP | Jumlah alamat host yang **di luar** rentang DHCP |
| 6 | `192.168.20.200` — Ya/Tidak | `10.4.7.300` — Ya/Tidak |
| 7 | `192.168.21.57` — Ya/Tidak | `10.4.8.130` — Ya/Tidak |
| 8 | `192.168.20.256` — Ya/Tidak | `10.4.7.9` — Ya/Tidak |

Pertanyaan 6–8: "Dapatkah alamat ini menjadi alamat perangkat lain di
jaringan yang sama dengan alamat perangkat di atas?"

## Yang diserahkan

Empat alamat (1–4), satu bilangan bulat (5), tiga jawaban Ya/Tidak (6–8).

## Penilaian

| Pemeriksaan | Aturan | Poin |
|---|---|---|
| c01–c04 | Alamat cocok persis (tanpa nol di depan, tanpa `/24`) | 4 × 5 = 20 |
| c05 | Bilangan bulat benar (boleh ditulis `… alamat`) | 5 |
| c06–c08 | Ya/Tidak benar | 3 × 5 = 15 |
| **Maksimum aktivitas** | | **40** |

## Kasus gagal

Kosong, alamat dengan nol di depan atau akhiran `/24`, angka dengan
desimal, atau jawaban selain Ya/Tidak → 0 untuk pemeriksaan itu; lainnya
tetap dinilai. Gangguan sistem → evaluasi diulang tanpa attempt baru.

## Umpan balik (setelah evaluasi)

Benar/salah per pertanyaan dan langkah perhitungan untuk varian yang kamu
kerjakan.

## Remedial

Varian lain menurut VA-2; ulangi Pelajaran 2 §3–§4 dan Pelajaran 4 §3;
materi remedial R-SUBNET.
