# DEBUG_REPORT.md - Penelusuran Bug PPN

**Masalah:** Harga akhir selalu lebih tinggi dari yang diharapkan setelah diskon.

**Langkah Debugging:**
1. Menjalankan `pdb.set_trace()` sebelum baris `return harga_akhir`.
2. Perintah `p harga_setelah_diskon`: Output `90000.0` (Benar untuk harga 100rb diskon 10%).
3. Perintah `p harga_akhir`: Output `99000.0`. 
4. **Analisis:** Ditemukan variabel `harga_akhir` bertambah 10% dari `harga_setelah_diskon`.
5. **Akar Masalah:** Terdapat logika tambahan `+ (harga_setelah_diskon * 0.10)` yang secara tidak sengaja menambahkan PPN.