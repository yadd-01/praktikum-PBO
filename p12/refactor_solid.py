import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Konfigurasi Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)

@dataclass
class Mahasiswa:
    """Model data untuk menyimpan informasi mahasiswa

    Args:
        nama (str): Nama lengkap mahasiswa.
        sks (int): Jumlah SKS yang diambil.
        prasyarat_lulus (bool): Status kelulusan mata kuliah prasyarat.
    """
    nama: str
    sks: int
    prasyarat_lulus: bool

class IValidationRule(ABC):
    """Interface abstrak untuk aturan validasi registrasi."""
    
    @abstractmethod
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        """Menjalankan logika validasi.

        Args:
            mahasiswa (Mahasiswa): Objek mahasiswa yang akan divalidasi.

        Returns:
            bool: True jika valid, False jika tidak.
        """
        pass

class SksValidator(IValidationRule):
    """Validasi kepatuhan jumlah pengambilan SKS."""
    
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        if mahasiswa.sks <= 24:
            LOGGER.info(f"Validasi SKS {mahasiswa.nama}: Berhasil.")
            return True
        LOGGER.warning(f"Validasi SKS {mahasiswa.nama}: Gagal (SKS: {mahasiswa.sks}).")
        return False

class PrerequisiteValidator(IValidationRule):
    """Validasi status kelulusan mata kuliah prasyarat."""
    
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        if mahasiswa.prasyarat_lulus:
            LOGGER.info(f"Validasi Prasyarat {mahasiswa.nama}: Berhasil.")
            return True
        LOGGER.warning(f"Validasi Prasyarat {mahasiswa.nama}: Gagal.")
        return False

class FinancialValidator(IValidationRule):
    """Validasi status pembayaran keuangan mahasiswa."""
    
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        # Simulasi validasi keuangan
        LOGGER.info(f"Validasi Keuangan {mahasiswa.nama}: Lunas.")
        return True

class RegistrationService:
    """Layanan untuk mengoordinasikan proses registrasi mahasiswa."""
    
    def __init__(self, validators: list[IValidationRule]):
        """Inisialisasi layanan dengan daftar aturan validasi.

        Args:
            validators (list[IValidationRule]): Daftar objek validator (Dependency Injection).
        """
        self.validators = validators  

    def run_validation(self, mahasiswa: Mahasiswa):
        """Menjalankan seluruh rangkaian validasi untuk satu mahasiswa.

        Args:
            mahasiswa (Mahasiswa): Data mahasiswa yang diproses.
        """
        print(f"\n--- Memproses Registrasi: {mahasiswa.nama} ---")
        results = [v.validate(mahasiswa) for v in self.validators]
        
        if all(results):
            print("Status Akhir: Registrasi DITERIMA.")
        else:
            LOGGER.error(f"Registrasi {mahasiswa.nama} DITOLAK.")
            print("Status Akhir: Registrasi DITOLAK.")

if __name__ == "__main__":
    # Contoh Kasus: SKS melebihi batas dan Prasyarat belum terpenuhi
    mhs_andi = Mahasiswa("Andi", 26, False)
    
    aturan = [SksValidator(), PrerequisiteValidator(), FinancialValidator()]
    app = RegistrationService(aturan)
    
    app.run_validation(mhs_andi)