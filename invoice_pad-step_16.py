# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: InvoicePad
def generate_monthly_stats(invoices, payments):
    from collections import defaultdict
    stats = defaultdict(lambda: {'total': 0, 'paid': 0, 'overdue': 0})
    today = datetime.now().date()
    for inv in invoices:
        month_key = f"{inv['month']}/{inv['year']}"
        if inv['status'] == 'pending' and (today - date.fromisoformat(inv['due_date']).days > 30):
            stats[month_key]['overdue'] += 1
    for pay in payments:
        month_key = f"{pay['month']}/{pay['year']}"
        if pay['status'] == 'completed':
            stats[month_key]['paid'] += pay['amount']
    return dict(stats)
