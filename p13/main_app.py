import logging
from repositories import ProductRepository
from services import IPaymentProcessor, ShoppingCart, CashPayment, DebitCardPayment
from models import Product

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger('MAIN_APP')

class PosApp:
    """Kelas Orchestrator untuk mengoordinasi flow aplikasi (DIP)."""
    def __init__(self, repository: ProductRepository, payment_processor: IPaymentProcessor):
        self.repository = repository
        self.payment_processor = payment_processor # Dependency Injection [cite: 246]
        self.cart = ShoppingCart()
        LOGGER.info("POS Application Initialized.")

    def _display_menu(self):
        LOGGER.info("\n--- DAFTAR PRODUK ---")
        for p in self.repository.get_all():
            LOGGER.info(f"[{p.id}] {p.name} - Rp{p.price:,.0f}")

    def _handle_add_item(self):
        product_id = input("Masukkan ID Produk: ").strip().upper()
        product = self.repository.get_by_id(product_id)
        if not product:
            LOGGER.warning("Produk tidak ditemukan.")
            return
        try:
            qty = int(input("Jumlah (default 1): ") or "1")
            if qty <= 0: raise ValueError
            self.cart.add_item(product, qty)
        except ValueError:
            LOGGER.error("Jumlah tidak valid.")

    def _handle_checkout(self):
        total = self.cart.total_price
        if total == 0:
            LOGGER.warning("Keranjang kosong.")
            return
        
        LOGGER.info(f"Total Belanja: Rp{total:,.0f}")
        if self.payment_processor.process(total):
            LOGGER.info("TRANSAKSI BERHASIL.")
            self._print_receipt()
            self.cart = ShoppingCart() # Reset cart
        else:
            LOGGER.error("TRANSAKSI GAGAL.")

    def _print_receipt(self):
        LOGGER.info("\n--- STRUK PEMBELIAN ---")
        for item in self.cart.get_items():
            LOGGER.info(f"{item.product.name} x{item.quantity} = Rp{item.subtotal:,.0f}")
        LOGGER.info(f"TOTAL AKHIR: Rp{self.cart.total_price:,.0f}")
        LOGGER.info("-----------------------")

if __name__ == "__main__":
    repo = ProductRepository()
    
    # 5. PENYELESAIAN CHALLENGE: Ganti CashPayment menjadi DebitCardPayment [cite: 548]
    payment_method = DebitCardPayment() 
    
    app = PosApp(repository=repo, payment_processor=payment_method)

    while True:
        print("\nMenu:\n1. Tampilkan Produk\n2. Tambah ke Keranjang\n3. Checkout\n4. Keluar")
        choice = input("Pilih opsi (1-4): ")
        if choice == "1": app._display_menu()
        elif choice == "2": app._handle_add_item()
        elif choice == "3": app._handle_checkout()
        elif choice == "4": break
        else: LOGGER.warning("Pilihan tidak valid.")