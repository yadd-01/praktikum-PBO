# before_refactor.py
from dataclasses import dataclass

@dataclass
class Mahasiswa:
    nama: str
    sks: int
    prasyarat_lulus: bool
class ValidatorManager:
    def validasi_registrasi(self, mahasiswa: Mahasiswa, kriteria: str):
        print(f"--- Memulai Validasi untuk {mahasiswa.nama} ---")
        if kriteria == "sks":
            if mahasiswa.sks <= 24:
                print("Validasi SKS: Berhasil.")
                return True
            else:
                print("Validasi SKS: Gagal (Maksimal 24 SKS).")
                return False
        elif kriteria == "prasyarat":
            if mahasiswa.prasyarat_lulus:
                print("Validasi Prasyarat: Berhasil.")
                return True
            else:
                print("Validasi Prasyarat: Gagal (Belum memenuhi prasyarat).")
                return False
        else:
            print("Kriteria validasi tidak dikenal.")
            return False
if __name__ == "__main__":
    mhs = Mahasiswa("Budi", 25, False)
    validator = ValidatorManager()
    validator.validasi_registrasi(mhs, "sks")