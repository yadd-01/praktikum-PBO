from models.barang import Barang
from models.pelanggan import Pelanggan
from models.sistem_penjualan import SistemPenjualan
from models.laporan_penjualan import LaporanPenjualan
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu_utama():
    print("\n=== SISTEM PENJUALAN BARANG ELEKTRONIK ===")
    print("1. Kelola Data Barang")
    print("2. Kelola Data Pelanggan")
    print("3. Transaksi Penjualan")
    print("4. Restok Barang")
    print("5. Laporan dan Statistik")
    print("6. Simpan dan Backup Data")
    print("0. Keluar")
    return input("Pilih menu: ")

def tampilkan_menu_barang():
    print("\n=== KELOLA DATA BARANG ===")
    print("1. Lihat Semua Barang")
    print("2. Edit Barang")
    print("3. Hapus Barang")
    print("0. Kembali")
    return input("Pilih menu: ")

def tampilkan_menu_pelanggan():
    print("\n=== KELOLA DATA PELANGGAN ===")
    print("1. Tambah Pelanggan")
    print("2. Lihat Semua Pelanggan")
    print("3. Edit Pelanggan")
    print("4. Hapus Pelanggan")
    print("0. Kembali")
    return input("Pilih menu: ")

def main():
    sistem = SistemPenjualan()
    admin = Pelanggan("ADM001", "Admin", "admin@toko.com", "0800000000", "Toko Elektronik")
    sistem.set_admin(admin)
    sistem.penyimpanan.tambah_pelanggan(admin)
    
    if sistem.penyimpanan.muat_semua_data():
        print("Data berhasil dimuat!")
    else:
        print("Membuat data baru...")
        barang1 = Barang("B001", "Laptop ASUS ROG", 15000000, 5, "Laptop")
        barang2 = Barang("B002", "Smartphone Samsung S23", 12000000, 10, "Smartphone")
        barang3 = Barang("B003", "Tablet iPad Air", 8000000, 8, "Tablet")
        
        sistem.penyimpanan.tambah_barang(barang1)
        sistem.penyimpanan.tambah_barang(barang2)
        sistem.penyimpanan.tambah_barang(barang3)
        
        pelanggan1 = Pelanggan("P001", "yadi", "yad@email.com", "08123456789", "Jl.juanda1")
        sistem.penyimpanan.tambah_pelanggan(pelanggan1)
    
    while True:
        clear_screen()
        pilihan = tampilkan_menu_utama()
        
        if pilihan == "1":
            while True:
                clear_screen()
                pilihan_barang = tampilkan_menu_barang()
                
                if pilihan_barang == "1":
                    print("\n=== DAFTAR BARANG ===")
                    for barang in sistem.penyimpanan.daftar_barang:
                        print(barang.tampilkan_info())
                    input("Tekan Enter untuk melanjutkan...")
                
                elif pilihan_barang == "2":
                    print("\n=== EDIT BARANG ===")
                    id_barang = input("ID Barang yang akan diedit: ")
                    barang = sistem.penyimpanan.cari_barang(id_barang)
                    if barang:
                        print(f"Barang ditemukan: {barang.tampilkan_info()}")
                        nama = input(f"Nama baru ({barang.get_nama()}): ") or barang.get_nama()
                        harga = input(f"Harga baru ({barang.get_harga()}): ") or barang.get_harga()
                        kategori = input(f"Kategori baru ({barang.get_kategori()}): ") or barang.get_kategori()
                        
                        barang.set_nama(nama)
                        barang.set_harga(int(harga))
                        barang.set_kategori(kategori)
                        print("Barang berhasil diupdate!")
                    else:
                        print("Barang tidak ditemukan!")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif pilihan_barang == "3":
                    print("\n=== HAPUS BARANG ===")
                    id_barang = input("ID Barang yang akan dihapus: ")
                    barang = sistem.penyimpanan.cari_barang(id_barang)
                    if barang:
                        sistem.penyimpanan.daftar_barang.remove(barang)
                        print("Barang berhasil dihapus!")
                    else:
                        print("Barang tidak ditemukan!")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif pilihan_barang == "0":
                    break
        
        elif pilihan == "2":
            while True:
                clear_screen()
                pilihan_pelanggan = tampilkan_menu_pelanggan()
                
                if pilihan_pelanggan == "1":
                    print("\n=== TAMBAH PELANGGAN ===")
                    id_pelanggan = input("ID Pelanggan: ")
                    nama = input("Nama: ")
                    email = input("Email: ")
                    no_hp = input("No HP: ")
                    alamat = input("Alamat: ")
                    
                    pelanggan_baru = Pelanggan(id_pelanggan, nama, email, no_hp, alamat)
                    sistem.penyimpanan.tambah_pelanggan(pelanggan_baru)
                    print("Pelanggan berhasil ditambahkan!")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif pilihan_pelanggan == "2":
                    print("\n=== DAFTAR PELANGGAN ===")
                    for pelanggan in sistem.penyimpanan.daftar_pelanggan:
                        print(pelanggan.tampilkan_info())
                    input("Tekan Enter untuk melanjutkan...")
                
                elif pilihan_pelanggan == "3":
                    print("\n=== EDIT PELANGGAN ===")
                    id_pelanggan = input("ID Pelanggan yang akan diedit: ")
                    pelanggan = sistem.penyimpanan.cari_pelanggan(id_pelanggan)
                    if pelanggan:
                        print(f"Pelanggan ditemukan: {pelanggan.tampilkan_info()}")
                        nama = input(f"Nama baru ({pelanggan.get_nama()}): ") or pelanggan.get_nama()
                        email = input(f"Email baru ({pelanggan.get_email()}): ") or pelanggan.get_email()
                        no_hp = input(f"No HP baru ({pelanggan.get_no_hp()}): ") or pelanggan.get_no_hp()
                        alamat = input(f"Alamat baru ({pelanggan.get_alamat()}): ") or pelanggan.get_alamat()
                        
                        pelanggan.set_nama(nama)
                        pelanggan.set_email(email)
                        pelanggan.set_no_hp(no_hp)
                        pelanggan.set_alamat(alamat)
                        print("Pelanggan berhasil diupdate!")
                    else:
                        print("Pelanggan tidak ditemukan!")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif pilihan_pelanggan == "4":
                    print("\n=== HAPUS PELANGGAN ===")
                    id_pelanggan = input("ID Pelanggan yang akan dihapus: ")
                    pelanggan = sistem.penyimpanan.cari_pelanggan(id_pelanggan)
                    if pelanggan and pelanggan.get_id_pelanggan() != "ADM001":
                        sistem.penyimpanan.daftar_pelanggan.remove(pelanggan)
                        print("Pelanggan berhasil dihapus!")
                    else:
                        print("Pelanggan tidak ditemukan atau tidak dapat menghapus admin!")
                    input("Tekan Enter untuk melanjutkan...")
                
                elif pilihan_pelanggan == "0":
                    break
        
        elif pilihan == "3":
            print("\n=== TRANSAKSI PENJUALAN ===")
            print("Daftar Pelanggan:")
            for i, pelanggan in enumerate(sistem.penyimpanan.daftar_pelanggan, 1):
                print(f"{i}. {pelanggan.tampilkan_info()}")
            
            try:
                pilih_pelanggan = int(input("Pilih nomor pelanggan: ")) - 1
                if 0 <= pilih_pelanggan < len(sistem.penyimpanan.daftar_pelanggan):
                    pelanggan = sistem.penyimpanan.daftar_pelanggan[pilih_pelanggan]
                    
                    id_transaksi = f"T{len(sistem.penyimpanan.daftar_transaksi) + 1:03d}"
                    metode_bayar = input("Metode Pembayaran (Cash/Transfer/Kartu): ")
                    diskon = int(input("Diskon (%): ") or 0)
                    
                    transaksi = sistem.proses_transaksi_penjualan(id_transaksi, pelanggan, metode_bayar, diskon)
                    
                    while True:
                        print("\nDaftar Barang:")
                        for i, barang in enumerate(sistem.penyimpanan.daftar_barang, 1):
                            print(f"{i}. {barang.tampilkan_info()}")
                        
                        pilih_barang = int(input("Pilih nomor barang (0 untuk selesai): ")) - 1
                        if pilih_barang == -1:
                            break
                        
                        if 0 <= pilih_barang < len(sistem.penyimpanan.daftar_barang):
                            barang = sistem.penyimpanan.daftar_barang[pilih_barang]
                            jumlah = int(input("Jumlah: "))
                            transaksi.tambah_barang(barang, jumlah)
                        else:
                            print("Pilihan tidak valid!")
                    
                    if transaksi.proses_transaksi():
                        transaksi.cetak_struk()
                    else:
                        print("Transaksi gagal! Stok tidak mencukupi.")
                
                else:
                    print("Pilihan tidak valid!")
            except ValueError:
                print("Input tidak valid!")
            input("Tekan Enter untuk melanjutkan...")
        
        elif pilihan == "4":
            print("\n=== RESTOK BARANG ===")
            supplier = input("Nama Supplier: ")
            id_transaksi = f"R{len(sistem.penyimpanan.daftar_transaksi) + 1:03d}"
            
            transaksi_restok = sistem.proses_restok_barang(id_transaksi, supplier)
            
            while True:
                print("\n=== PILIHAN ===")
                print("1. Restok Barang Existing")
                print("2. Tambah Barang Baru + Restok")
                print("0. Selesai")
                pilihan_restok = input("Pilih: ")
                
                if pilihan_restok == "1":
                    print("\nDaftar Barang:")
                    for i, barang in enumerate(sistem.penyimpanan.daftar_barang, 1):
                        print(f"{i}. {barang.tampilkan_info()}")
                    
                    pilih_barang = int(input("Pilih nomor barang: ")) - 1
                    if 0 <= pilih_barang < len(sistem.penyimpanan.daftar_barang):
                        barang = sistem.penyimpanan.daftar_barang[pilih_barang]
                        jumlah = int(input("Jumlah restok: "))
                        transaksi_restok.tambah_barang(barang, jumlah)
                    else:
                        print("Pilihan tidak valid!")
                
                elif pilihan_restok == "2":
                    print("\n=== TAMBAH BARANG BARU ===")
                    id_barang = input("ID Barang: ")
                    nama = input("Nama Barang: ")
                    harga = int(input("Harga: "))
                    stok = int(input("Stok Awal: "))
                    kategori = input("Kategori: ")
                    
                    if transaksi_restok.tambah_barang_baru(id_barang, nama, harga, stok, kategori, sistem):
                        print("Barang baru berhasil ditambahkan dan diretok!")
                    else:
                        print("Gagal menambah barang baru!")
                
                elif pilihan_restok == "0":
                    break
                else:
                    print("Pilihan tidak valid!")
            
            if transaksi_restok.proses_transaksi():
                transaksi_restok.cetak_info_restok()
            input("Tekan Enter untuk melanjutkan...")
        
        elif pilihan == "5":
            print("\n=== LAPORAN DAN STATISTIK ===")
            laporan = LaporanPenjualan(sistem)
            
            print("\n" + laporan.buat_ringkasan())
            
            statistik = laporan.hitung_statistik()
            if statistik:
                print("\nStatistik Penjualan per Barang:")
                for barang, jumlah in statistik.items():
                    print(f"- {barang}: {jumlah} unit")
            else:
                print("\nBelum ada data penjualan.")
            
            if input("\nSimpan laporan ke file? (y/n): ").lower() == 'y':
                if laporan.simpan_laporan():
                    print("Laporan berhasil disimpan!")
            
            input("Tekan Enter untuk melanjutkan...")
        
        elif pilihan == "6":
            print("\n=== SIMPAN DAN BACKUP DATA ===")
            sistem.penyimpanan.simpan_semua_data()
            print("Data berhasil disimpan!")
            
            if sistem.penyimpanan.buat_backup():
                print("Backup data berhasil dibuat!")
            else:
                print("Gagal membuat backup!")
            
            input("Tekan Enter untuk melanjutkan...")
        
        elif pilihan == "0":
            sistem.penyimpanan.simpan_semua_data()
            print("Terima kasih! Data telah disimpan.")
            break

if __name__ == "__main__":
    main()