# Laporan Praktikum SOLID - Sistem Validasi Registrasi Mahasiswa



[cite_start]Repositori ini disusun untuk memenuhi tugas Modul Praktikum 11 mengenai **Refactoring Struktur Kode Menggunakan Prinsip SOLID**[cite: 1, 2]. [cite_start]Proyek ini mendemonstrasikan proses transformasi kode dari struktur monolitik (*God Class*) menjadi struktur yang modular dan *maintainable*[cite: 6, 12].



## 1. Pendahuluan

[cite_start]Tujuan utama praktikum ini adalah menganalisis "Code Smell" dan menerapkan prinsip desain SOLID, khususnya **Single Responsibility Principle (SRP)**, **Open/Closed Principle (OCP)**, dan **Dependency Inversion Principle (DIP)**[cite: 5, 6].



## 2. Studi Kasus

Sistem yang dikembangkan adalah **Validator Registrasi Mahasiswa**. Sistem ini bertugas memvalidasi kelayakan mahasiswa berdasarkan:

* [cite_start]Jumlah SKS yang diambil[cite: 203].

* [cite_start]Kelulusan mata kuliah prasyarat[cite: 203].

* Status pembayaran keuangan (sebagai fitur tambahan/challenge).



## 3. Analisis Kode Sebelum Refactoring (`before_refactor.py`)

Pada tahap awal, kode menggunakan satu kelas besar (`ValidatorManager`) yang memiliki masalah sebagai berikut:

* [cite_start]**Single Responsibility Principle (SRP):** Kelas ini memiliki lebih dari satu tanggung jawab karena mengelola logika SKS sekaligus prasyarat dalam satu tempat[cite: 9, 16].

* [cite_start]**Open/Closed Principle (OCP):** Penambahan aturan validasi baru mengharuskan modifikasi pada percabangan `if/else` di dalam metode utama, yang membuat kode menjadi kaku dan rapuh[cite: 18, 19, 25].

* [cite_start]**Dependency Inversion Principle (DIP):** Logika bisnis tingkat tinggi bergantung langsung pada detail implementasi konkret (hardcoded), bukan pada abstraksi[cite: 27, 84].



## 4. Implementasi Refactoring (`after_refactor.py`)

[cite_start]Refactoring dilakukan dengan memecah kelas besar menjadi beberapa kelas kecil yang memiliki tanggung jawab tunggal[cite: 23].



### Langkah-langkah yang Diterapkan:

1.  [cite_start]**Abstraksi (Interface):** Membuat kontrak `IValidationRule` menggunakan `Abstract Class` sebagai standar untuk semua aturan validasi[cite: 10, 105].

2.  [cite_start]**Penerapan SRP:** Memisahkan `SksValidator` dan `PrerequisiteValidator` menjadi kelas mandiri[cite: 21, 114].

3.  [cite_start]**Dependency Injection (DIP):** Menyuntikkan daftar aturan validasi ke dalam `RegistrationService` melalui constructor agar kelas koordinator tidak bergantung pada detail implementasi[cite: 38, 150].







## 5. Hasil Pengujian (Pembuktian OCP)

[cite_start]Sesuai dengan prinsip OCP, fitur baru bernama `FinancialValidator` berhasil ditambahkan tanpa mengubah kode yang sudah ada pada kelas `RegistrationService`[cite: 11, 183]. Sistem tetap berjalan dengan baik dengan menyuntikkan objek validator baru tersebut.



### Screenshot Output Terminal

*(Gantikan teks ini dengan gambar screenshot Anda setelah menjalankan program)*

![Output Terminal](screenshot_output.png)



## 6. Kesimpulan & Refleksi

Pendekatan **Dependency Injection (DI)** terbukti lebih efektif dibandingkan metode `if/else` karena:

* [cite_start]**Mencegah Code Smell:** Menghindari kelas yang terlalu besar (*God Class*)[cite: 15, 212].

* [cite_start]**Fleksibilitas:** Memungkinkan penambahan fitur baru (ekstensi) tanpa risiko merusak fitur lama (modifikasi)[cite: 25, 161].

* [cite_start]**Kerapihan:** Kode menjadi lebih modular, mudah dibaca, dan mudah untuk diuji secara terpisah[cite: 6, 12].



---

**Identitas Praktikan:**

* **Nama:** Ariyadi

* **NIM:** 2411102441240

* **Kelas:** B