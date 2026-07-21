# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: InvoicePad
def print_project_metrics():
    total_invoices = len(invoices)
    paid_count = sum(1 for inv in invoices if inv.get('paid', False))
    overdue_count = sum(1 for inv in invoices if inv.get('due_date') and invite_due_date < datetime.now().date())
    total_amount = sum(inv.get('amount', 0) for inv in invoices)
    paid_total = sum(inv.get('paid_amount', 0) for inv in invoices)
    unique_clients = len(set(inv.get('client_name', '') for inv in invoices if inv.get('client_name')))

    print(f"Total Invoices: {total_invoices}")
    print(f"Paid Invoices: {paid_count}/{total_invoices} ({(paid_count/total_invoices*100) if total_invoices else 0:.1f}%)")
    print(f"Overdue Invoices: {overdue_count}")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Paid Amount: ${paid_total:.2f}")
    print(f"Outstanding: ${total_amount - paid_total:.2f}")
    print(f"Unique Clients: {unique_clients}")

print_project_metrics()
