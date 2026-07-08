# === Stage 20: Добавь восстановление записей из архива ===
# Project: InvoicePad
def restore_from_archive():
    """Восстанавливает записи из архива в активные данные."""
    print("Загрузка записей из архива...")
    with open('archive.txt', 'r') as f:
        lines = f.readlines()
    records = []
    for line in lines:
        parts = line.strip().split('|')
        if len(parts) != 6:
            continue
        client_id, invoice_date, amount, payment, due_date, notes = parts
        status = 'inactive'
        record = {'client_id': int(client_id), 'invoice_date': invoice_date, 'amount': float(amount), 'payment': float(payment), 'due_date': due_date, 'notes': notes, 'status': status}
        records.append(record)
    with open('records.txt', 'w') as f:
        for r in records:
            f.write(f"{r['client_id']}|{r['invoice_date']}|{r['amount']:.2f}|{r['payment']:.2f}|{r['due_date']}|{r['notes']}|{r['status']}\n")
    print(f"Восстановлено {len(records)} записей из архива.")
