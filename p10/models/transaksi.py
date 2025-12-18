from abc import ABC, abstractmethod
from datetime import datetime

class Transaksi(ABC):
    def __init__(self, id_transaksi, pelanggan):
        self.__id_transaksi = id_transaksi
        self.__pelanggan = pelanggan
        self.__tanggal = datetime.now()
        self.__daftar_barang = []
    
    def get_id_transaksi(self):
        return self.__id_transaksi
    
    def get_pelanggan(self):
        return self.__pelanggan
    
    def get_tanggal(self):
        return self.__tanggal
    
    def get_daftar_barang(self):
        return self.__daftar_barang
    
    def tambah_barang(self, barang, jumlah):
        self.__daftar_barang.append((barang, jumlah))
    
    def hitung_total(self):
        total = 0
        for barang, jumlah in self.__daftar_barang:
            total += barang.get_harga() * jumlah
        return total
    
    @abstractmethod
    def proses_transaksi(self):
        pass