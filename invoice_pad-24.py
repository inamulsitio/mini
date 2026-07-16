# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: InvoicePad
def print_invoice_record(record):
    """Компактный вывод одной записи счета."""
    if not record:
        return "Запись пуста."
    line = (f"Инвойс #{record.get('invoice_id') or 'N/A'} | "
            f"Клиент: {record.get('client_name', 'Не указан')} | "
            f"Сумма: {record.get('amount', 0):,.2f} руб. | "
            f"Оплачено: {record.get('paid_amount', 0):,.2f} руб.")
    if record.get("due_date"):
        line += f" | Срок: {record['due_date']}"
    if record.get("notes"):
        line += f" | Заметка: {record['notes'][:50]}"
    print(line)


def main():
    invoices = [
        {"invoice_id": 1, "client_name": "ООО Ромашка", "amount": 15000.00, "paid_amount": 5000.00, "due_date": "2024-06-30", "notes": "Первая партия"},
        {"invoice_id": 2, "client_name": "ИП Иванов", "amount": 8500.00, "paid_amount": 8500.00, "due_date": "2024-05-15", "notes": ""},
    ]
    for inv in invoices:
        print_invoice_record(inv)


if __name__ == "__main__":
    main()
