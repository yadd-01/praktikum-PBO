# after_refactor.py
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Mahasiswa:
    nama: str
    sks: int
    prasyarat_lulus: bool
class IValidationRule(ABC):
    @abstractmethod
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        pass
class SksValidator(IValidationRule):
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        if mahasiswa.sks <= 24:
            print(f"Validasi SKS {mahasiswa.nama}: Berhasil.")
            return True
        print(f"Validasi SKS {mahasiswa.nama}: Gagal.")
        return False
class PrerequisiteValidator(IValidationRule):
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        if mahasiswa.prasyarat_lulus:
            print(f"Validasi Prasyarat {mahasiswa.nama}: Berhasil.")
            return True
        print(f"Validasi Prasyarat {mahasiswa.nama}: Gagal.")
        return False
class RegistrationService:
    def __init__(self, validators: list[IValidationRule]):
        self.validators = validators  
    def run_validation(self, mahasiswa: Mahasiswa):
        print(f"--- Memproses Registrasi: {mahasiswa.nama} ---")
        results = [v.validate(mahasiswa) for v in self.validators]
        if all(results):
            print("Status Akhir: Registrasi DITERIMA.")
        else:
            print("Status Akhir: Registrasi DITOLAK.")
class FinancialValidator(IValidationRule):
    def validate(self, mahasiswa: Mahasiswa) -> bool:
        print(f"Validasi Keuangan {mahasiswa.nama}: Lunas.")
        return True
if __name__ == "__main__":
    mhs_andi = Mahasiswa("Andi", 26, False)
    aturan = [SksValidator(), PrerequisiteValidator(), FinancialValidator()]
    app = RegistrationService(aturan)
    app.run_validation(mhs_andi)