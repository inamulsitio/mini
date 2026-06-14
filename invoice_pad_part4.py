# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: InvoicePad
def edit_invoice(invoice_id: int, updates: dict) -> InvoiceRecord | None:
    for i, inv in enumerate(INVOICES):
        if inv.id == invoice_id:
            new_inv = InvoiceRecord(
                id=inv.id,
                client_name=updates.get("client_name", inv.client_name),
                amount=updates.get("amount", inv.amount),
                due_date=updates.get("due_date", inv.due_date),
                notes=updates.get("notes", inv.notes),
                paid=updates.get("paid", inv.paid)
            )
            INVOICES[i] = new_inv
            print(f"Счёт #{invoice_id} обновлён.")
            return new_inv
    print(f"Счёт #{invoice_id} не найден.")
    return None
