import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):
    
    def setUp(self):
        """Arrange: Inisialisasi objek sebelum setiap tes."""
        self.calc = DiskonCalculator()

    def test_diskon_normal(self):
        """Uji kondisi normal: Diskon 10% dari 100.000 (Tanpa PPN harusnya 90.000)."""
        # Setelah bug PPN diperbaiki di calculator.py, hasil harus 90000
        self.assertEqual(self.calc.hitung_diskon(100000, 10), 90000)

    def test_diskon_0_persen(self):
        """Boundary Condition: Batas bawah diskon 0%."""
        self.assertEqual(self.calc.hitung_diskon(50000, 0), 50000)

    def test_diskon_100_persen(self):
        """Boundary Condition: Batas atas diskon 100%."""
        self.assertEqual(self.calc.hitung_diskon(50000, 100), 0)

    def test_nilai_float(self):
        """Tahap 4: Uji presisi angka desimal."""
        # Diskon 33% dari 999 = 669.33
        self.assertAlmostEqual(self.calc.hitung_diskon(999, 33), 669.33, places=2)

    def test_edge_case_harga_nol(self):
        """Tahap 4: Edge Case harga awal 0."""
        self.assertEqual(self.calc.hitung_diskon(0, 10), 0)

if __name__ == "__main__":
    unittest.main()