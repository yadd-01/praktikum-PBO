from models.transaksi import Transaksi
from models.barang import Barang

class TransaksiRestok(Transaksi):
    def __init__(self, id_transaksi, pelanggan, supplier):
        super().__init__(id_transaksi, pelanggan)
        self.__supplier = supplier
    
    def get_supplier(self):
        return self.__supplier
    
    def proses_transaksi(self):
        for barang, jumlah in self.get_daftar_barang():
            barang.tambah_stok(jumlah)
        print(f"Restok dari {self.__supplier} berhasil!")
        return True
    
    def tambah_barang_baru(self, id_barang, nama, harga, stok, kategori, sistem):
        barang_existing = sistem.penyimpanan.cari_barang(id_barang)
        if barang_existing:
            print(f"Barang dengan ID {id_barang} sudah ada!")
            return False
        
        barang_baru = Barang(id_barang, nama, harga, stok, kategori)
        sistem.penyimpanan.tambah_barang(barang_baru)
        self.tambah_barang(barang_baru, stok)
        print(f"Barang baru berhasil ditambahkan: {nama}")
        return True
    
    def cetak_info_restok(self):
        print(f"\n=== INFO RESTOK ===")
        print(f"ID: {self.get_id_transaksi()}")
        print(f"Supplier: {self.__supplier}")
        print(f"Tanggal: {self.get_tanggal().strftime('%d-%m-%Y %H:%M')}")
        print("Barang:")
        for barang, jumlah in self.get_daftar_barang():
            print(f"- {barang.get_nama()} x{jumlah}")
        print("=" * 30)