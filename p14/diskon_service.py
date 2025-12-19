import pdb

class DiskonCalculator:
    """Kelas untuk menghitung diskon dan harga akhir."""
    
    def hitung_diskon(self, harga_awal: float, persen_diskon: float) -> float:
        """
        Menghitung harga akhir setelah diskon.
        
        Args:
            harga_awal (float): Harga barang sebelum diskon.
            persen_diskon (float): Besar diskon dalam persen (0-100).
            
        Returns:
            float: Harga akhir setelah dipotong diskon.
        """
        
        # Langkah Debugging (Gunakan p harga_awal atau p persen_diskon di terminal)
        # pdb.set_trace() 
        
        # Validasi Input (Edge Case)
        if harga_awal <= 0:
            return 0.0
            
        # Perbaikan Bug: Pastikan persen dibagi 100
        jumlah_diskon = harga_awal * (persen_diskon / 100)
        
        # Perbaikan Bug: Hapus baris PPN 10% yang menyebabkan test FAIL
        harga_akhir = harga_awal - jumlah_diskon
        
        return harga_akhir