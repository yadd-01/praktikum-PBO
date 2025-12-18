class Barang:
    def __init__(self, id_barang, nama, harga, stok, kategori):
        self.__id_barang = id_barang
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok
        self.__kategori = kategori
    
    def get_id_barang(self):
        return self.__id_barang
    
    def get_nama(self):
        return self.__nama
    
    def get_harga(self):
        return self.__harga
    
    def get_stok(self):
        return self.__stok
    
    def get_kategori(self):
        return self.__kategori
    
    def set_nama(self, nama):
        self.__nama = nama
    
    def set_harga(self, harga):
        self.__harga = harga
    
    def set_kategori(self, kategori):
        self.__kategori = kategori
    
    def tambah_stok(self, jumlah):
        self.__stok += jumlah
    
    def kurangi_stok(self, jumlah):
        if self.__stok >= jumlah:
            self.__stok -= jumlah
            return True
        return False
    
    def tampilkan_info(self):
        return f"ID: {self.__id_barang} | {self.__nama} | Rp {self.__harga:,} | Stok: {self.__stok} | {self.__kategori}"