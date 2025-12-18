from models.penyimpanan_data import PenyimpananData
from models.transaksi_penjualan import TransaksiPenjualan
from models.transaksi_restok import TransaksiRestok

class SistemPenjualan:
    def __init__(self):
        self.penyimpanan = PenyimpananData()
        self.admin = None
    
    def set_admin(self, admin):
        self.admin = admin
    
    def jalankan_sistem(self):
        print("Sistem Penjualan Barang Elektronik dijalankan")
    
    def proses_transaksi_penjualan(self, id_transaksi, pelanggan, metode_pembayaran, diskon=0):
        transaksi = TransaksiPenjualan(id_transaksi, pelanggan, metode_pembayaran, diskon)
        self.penyimpanan.tambah_transaksi(transaksi)
        return transaksi
    
    def proses_restok_barang(self, id_transaksi, supplier):
        transaksi = TransaksiRestok(id_transaksi, self.admin, supplier)
        self.penyimpanan.tambah_transaksi(transaksi)
        return transaksi