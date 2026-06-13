# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: InvoicePad
class InvoicePad:
    def __init__(self):
        self.clients = {}
        self.invoices = []

    def add_client(self, name, email=None):
        if not name: raise ValueError("Имя клиента обязательно")
        self.clients[name] = {"email": email or "", "notes": ""}
        return self.clients[name]["email"]

    def create_invoice(self, client_name, amount, due_date, notes=""):
        if client_name not in self.clients: raise KeyError(f"Клиент {client_name} не найден")
        invoice_id = len(self.invoices) + 1
        status = "pending" if int(due_date.split('-')[2]) < 30 else "paid"
        self.invoices.append({
            "id": invoice_id,
            "client": client_name,
            "amount": float(amount),
            "due_date": due_date,
            "status": status,
            "notes": notes
        })
        return invoice_id

    def mark_paid(self, invoice_id):
        for inv in self.invoices:
            if inv["id"] == invoice_id and inv["status"] != "paid":
                inv["status"] = "paid"
                return True
        return False
