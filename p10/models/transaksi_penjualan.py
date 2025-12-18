from models.transaksi import Transaksi

class TransaksiPenjualan(Transaksi):
    def __init__(self, id_transaksi, pelanggan, metode_pembayaran, diskon=0):
        super().__init__(id_transaksi, pelanggan)
        self.__metode_pembayaran = metode_pembayaran
        self.__diskon = diskon
    
    def get_metode_pembayaran(self):
        return self.__metode_pembayaran
    
    def get_diskon(self):
        return self.__diskon
    
    def hitung_total(self):
        total = super().hitung_total()
        return total - (total * self.__diskon / 100)
    
    def proses_transaksi(self):
        for barang, jumlah in self.get_daftar_barang():
            if not barang.kurangi_stok(jumlah):
                return False
        self.get_pelanggan().tambah_riwayat(self)
        return True
    
    def cetak_struk(self):
        print(f"\n=== STRUK PENJUALAN ===")
        print(f"ID Transaksi: {self.get_id_transaksi()}")
        print(f"Tanggal: {self.get_tanggal().strftime('%d-%m-%Y %H:%M')}")
        print(f"Pelanggan: {self.get_pelanggan().get_nama()}")
        print(f"Metode Bayar: {self.__metode_pembayaran}")
        print("Barang:")
        for barang, jumlah in self.get_daftar_barang():
            print(f"- {barang.get_nama()} x{jumlah} = Rp {barang.get_harga() * jumlah:,}")
        print(f"Subtotal: Rp {super().hitung_total():,}")
        print(f"Diskon: {self.__diskon}%")
        print(f"TOTAL: Rp {self.hitung_total():,}")
        print("=" * 30)