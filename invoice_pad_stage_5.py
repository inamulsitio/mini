# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: InvoicePad
def delete_invoice(invoice_id):
    if invoice_id not in invoices:
        print(f"Счёт #{invoice_id} не найден.")
        return False
    deleted = invoices.pop(invoice_id)
    print(f"Счёт #{deleted['id']} удалён. Клиент: {deleted['client_name']}, сумма: {deleted['amount']}.")
    return True

def delete_client(client_id):
    if client_id not in clients:
        print(f"Клиент #{client_id} не найден.")
        return False
    deleted = clients.pop(client_id)
    # Удаляем связанные счета клиента, если нужно (опционально), здесь просто выводим сообщение
    count_deleted_invoices = sum(1 for inv in invoices.values() if inv['client_id'] == client_id)
    print(f"Клиент #{deleted['id']} удалён. Было связано {count_deleted_invoices} счетов.")
    return True

def delete_payment(payment_id):
    if payment_id not in payments:
        print(f"Оплата #{payment_id} не найдена.")
        return False
    deleted = payments.pop(payment_id)
    # Обновляем статус счета, если оплата была привязана к нему (логика зависит от структуры данных)
    # Предположим, что в объекте payment есть ссылка на invoice_id
    if 'invoice_id' in deleted:
        inv_id = deleted['invoice_id']
        if inv_id in invoices:
            invoices[inv_id]['status'] = 'paid'  # Или другая логика статуса
    print(f"Оплата #{deleted['id']} удалена.")
    return True

def delete_note(note_id):
    if note_id not in notes:
        print(f"Заметка #{note_id} не найдена.")
        return False
    deleted = notes.pop(note_id)
    # Удаляем заметку из соответствующего счета или клиента, если она там хранилась отдельно
    # Здесь предположим, что note хранится в отдельном словаре notes с ключом id
    print(f"Заметка #{deleted['id']} удалена.")
    return True
