# Registrasi Mahasiswa - SOLID, Logging & Docstrings (Pertemuan 12)

Proyek ini merupakan pengembangan dari sistem validasi registrasi mahasiswa pada Pertemuan 11. Fokus utama pada tahap ini adalah meningkatkan profesionalitas kode melalui penerapan **Google Style Docstrings**, sistem **Logging** untuk pelacakan aktivitas, dan manajemen riwayat perubahan menggunakan **Git**.

## 1. Pendahuluan
Tujuan praktikum Pertemuan 12 adalah:
* Menerapkan dokumentasi kode yang standar menggunakan Docstrings.
* Mengganti output sistem (`print`) dengan `logging` yang memiliki level (INFO, WARNING, ERROR).
* Mengelola proyek menggunakan Version Control System (Git & GitHub).

## 2. Fitur dan Pembaruan (Pertemuan 12)
### A. Professional Logging
Sistem tidak lagi menggunakan `print()` untuk log internal. Kami menerapkan modul `logging` dengan format: `%(asctime)s - %(levelname)s - %(message)s`.
* **INFO**: Mencatat keberhasilan validasi.
* **WARNING**: Mencatat jika mahasiswa tidak memenuhi kriteria (SKS berlebih atau prasyarat gagal).
* **ERROR**: Mencatat kegagalan fatal yang menyebabkan registrasi ditolak.

### B. Google Style Docstrings
Setiap kelas dan metode dalam `refactor_solid.py` kini dilengkapi dokumentasi lengkap yang mencakup:
* **Deskripsi**: Penjelasan fungsi komponen.
* **Args**: Penjelasan parameter yang diterima.
* **Returns**: Penjelasan nilai yang dikembalikan oleh fungsi.


## 3. Analisis SOLID (Review Pertemuan 11)
Proyek ini tetap mempertahankan prinsip SOLID:

SRP: Setiap validator (SKS, Prasyarat, Keuangan) berada di kelas terpisah.

OCP: Menambah validator baru (FinancialValidator) tanpa mengubah kelas RegistrationService.

DIP: RegistrationService bergantung pada abstraksi IValidationRule.

## 4. Riwayat Perubahan (Git Commit)
Proyek ini dikelola dengan Git untuk mencatat riwayat pengembangan:

Initial commit: Inisialisasi struktur SOLID dari Pertemuan 11.

Docs: Implementasi Google Style Docstrings pada seluruh kelas.

Feat: Migrasi ke sistem Logging dan pengaturan tingkat severity (INFO/WARNING/ERROR).

## 5. Cara Menjalankan
Pastikan Python 3.x terinstal.

Jalankan perintah berikut di terminal:

Bash

python refactor_solid.py
## 6. Refleksi
Penggunaan Docstrings sangat krusial dalam kolaborasi tim karena berfungsi sebagai manual internal bagi pengembang lain. Sementara itu, Logging jauh lebih efektif daripada if/else atau print biasa dalam mencegah Code Smell karena logging memungkinkan kita memfilter informasi berdasarkan tingkat kepentingannya dan menyimpan histori eksekusi secara otomatis ke dalam file eksternal jika diperlukan, sehingga memudahkan proses debugging pada sistem yang kompleks.


Identitas Praktikan:

Nama: Ariyadi
NIM: 2411102441240
Kelas: B


