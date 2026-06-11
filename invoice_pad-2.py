# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: InvoicePad
class InvoicePad:
    def __init__(self):
        self.clients = {}
        self.invoices = []

    def validate_client_name(self, name):
        if not isinstance(name, str) or len(name.strip()) < 2:
            raise ValueError("Имя клиента должно быть строкой длиной не менее 2 символов.")
        return name.strip()

    def validate_amount(self, amount):
        try:
            val = float(amount)
            if val < 0:
                raise ValueError("Сумма счета не может быть отрицательной.")
            return round(val, 2)
        except (ValueError, TypeError):
            raise ValueError("Некорректный формат суммы. Ожидаются цифры.")

    def validate_date(self, date_str):
        try:
            from datetime import datetime
            if not isinstance(date_str, str):
                raise ValueError("Дата должна быть строкой.")
            # Парсинг формата YYYY-MM-DD или DD.MM.YYYY
            for fmt in ("%Y-%m-%d", "%d.%m.%Y"):
                try:
                    return datetime.strptime(date_str.strip(), fmt).date()
                except ValueError:
                    continue
            raise ValueError("Неверный формат даты. Используйте YYYY-MM-DD или DD.MM.YYYY.")
        except Exception as e:
            if "некорректное значение" in str(e):
                raise ValueError("Ошибка парсинга даты.")
            return date_str

    def add_client(self, name, email=None):
        validated_name = self.validate_client_name(name)
        self.clients[validated_name] = {"email": email or "", "notes": ""}
        return True

    def create_invoice(self, client_name, amount, due_date, notes=""):
        if client_name not in self.clients:
            raise ValueError(f"Клиент '{client_name}' не найден.")
        validated_amount = self.validate_amount(amount)
        validated_due_date = self.validate_date(due_date)
        invoice_id = len(self.invoices) + 1
        new_invoice = {
            "id": invoice_id,
            "client": client_name,
            "amount": validated_amount,
            "due_date": validated_due_date,
            "notes": notes,
            "status": "pending"
        }
        self.invoices.append(new_invoice)
        return new_invoice

    def record_payment(self, invoice_id, paid_amount):
        try:
            amount = float(paid_amount)
        except (ValueError, TypeError):
            raise ValueError("Сумма оплаты должна быть числом.")
        if amount <= 0:
            raise ValueError("Сумма оплаты не может быть отрицательной или нулевой.")
        
        for inv in self.invoices:
            if inv["id"] == invoice_id:
                remaining = inv["amount"] - amount
                if remaining < 0:
                    raise ValueError(f"Переплата. Остаток по счету {invoice_id} составляет {inv['amount']}.")
                inv["paid_amount"] += amount
                inv["status"] = "paid" if remaining <= 0 else "partial"
                return True
        raise
