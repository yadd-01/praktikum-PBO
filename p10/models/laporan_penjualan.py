class LaporanPenjualan:
    def __init__(self, sistem_penjualan):
        self.sistem = sistem_penjualan
    
    def buat_ringkasan(self):
        total_penjualan = 0
        total_transaksi = 0
        
        for transaksi in self.sistem.penyimpanan.daftar_transaksi:
            if hasattr(transaksi, 'hitung_total'):
                total_penjualan += transaksi.hitung_total()
                total_transaksi += 1
        
        return f"Total Penjualan: Rp {total_penjualan:,}\nTotal Transaksi: {total_transaksi}"
    
    def simpan_laporan(self):
        ringkasan = self.buat_ringkasan()
        with open('laporan_penjualan.txt', 'w') as f:
            f.write(ringkasan)
        return True
    
    def hitung_statistik(self):
        statistik = {}
        for transaksi in self.sistem.penyimpanan.daftar_transaksi:
            if hasattr(transaksi, 'get_daftar_barang'):
                for barang, jumlah in transaksi.get_daftar_barang():
                    nama_barang = barang.get_nama()
                    if nama_barang in statistik:
                        statistik[nama_barang] += jumlah
                    else:
                        statistik[nama_barang] = jumlah
        return statistik