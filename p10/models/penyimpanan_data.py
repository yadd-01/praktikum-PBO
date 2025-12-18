import json
from models.barang import Barang
from models.pelanggan import Pelanggan

class PenyimpananData:
    def __init__(self):
        self.daftar_barang = []
        self.daftar_pelanggan = []
        self.daftar_transaksi = []
    
    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)
    
    def tambah_pelanggan(self, pelanggan):
        self.daftar_pelanggan.append(pelanggan)
    
    def tambah_transaksi(self, transaksi):
        self.daftar_transaksi.append(transaksi)
    
    def cari_barang(self, id_barang):
        for barang in self.daftar_barang:
            if barang.get_id_barang() == id_barang:
                return barang
        return None
    
    
    
    def cari_pelanggan(self, id_pelanggan):
        for pelanggan in self.daftar_pelanggan:
            if pelanggan.get_id_pelanggan() == id_pelanggan:
                return pelanggan
        return None
    
    def simpan_semua_data(self):
        data = {
            'barang': [
                {
                    'id_barang': b.get_id_barang(),
                    'nama': b.get_nama(),
                    'harga': b.get_harga(),
                    'stok': b.get_stok(),
                    'kategori': b.get_kategori()
                } for b in self.daftar_barang
            ],
            'pelanggan': [
                {
                    'id_pelanggan': p.get_id_pelanggan(),
                    'nama': p.get_nama(),
                    'email': p.get_email(),
                    'no_hp': p.get_no_hp(),
                    'alamat': p.get_alamat()
                } for p in self.daftar_pelanggan
            ]
        }
        with open('data_sistem.json', 'w') as f:
            json.dump(data, f, indent=2)
    
    def muat_semua_data(self):
        try:
            with open('data_sistem.json', 'r') as f:
                data = json.load(f)
            
            self.daftar_barang = [
                Barang(b['id_barang'], b['nama'], b['harga'], b['stok'], b['kategori'])
                for b in data['barang']
            ]
            
            self.daftar_pelanggan = [
                Pelanggan(p['id_pelanggan'], p['nama'], p['email'], p['no_hp'], p['alamat'])
                for p in data['pelanggan']
            ]
            
            return True
        except:
            return False
    
    def buat_backup(self):
        import shutil
        try:
            shutil.copy2('data_sistem.json', 'backup_data.json')
            return True
        except:
            return False