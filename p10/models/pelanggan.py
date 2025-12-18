class Pelanggan:
    def __init__(self, id_pelanggan, nama, email, no_hp, alamat):
        self.__id_pelanggan = id_pelanggan
        self.__nama = nama
        self.__email = email
        self.__no_hp = no_hp
        self.__alamat = alamat
        self.__riwayat_belanja = []
    
    def get_id_pelanggan(self):
        return self.__id_pelanggan
    
    def get_nama(self):
        return self.__nama
    
    def get_email(self):
        return self.__email
    
    def get_no_hp(self):
        return self.__no_hp
    
    def get_alamat(self):
        return self.__alamat
    
    def get_riwayat_belanja(self):
        return self.__riwayat_belanja
    
    def set_nama(self, nama):
        self.__nama = nama
    
    def set_email(self, email):
        self.__email = email
    
    def set_no_hp(self, no_hp):
        self.__no_hp = no_hp
    
    def set_alamat(self, alamat):
        self.__alamat = alamat
    
    def tambah_riwayat(self, transaksi):
        self.__riwayat_belanja.append(transaksi)
    
    def tampilkan_info(self):
        return f"ID: {self.__id_pelanggan} | {self.__nama} | {self.__email} | {self.__no_hp}"