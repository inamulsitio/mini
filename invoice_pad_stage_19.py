# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: InvoicePad
def archive_invoice(invoice):
    invoice['status'] = 'archived'
    if 'archive_date' not in invoice:
        from datetime import date, timedelta
        invoice['archive_date'] = (date.today() - timedelta(days=30)).isoformat()
    return invoice

def list_archived_invoices(invoices):
    archived = [inv for inv in invoices if inv.get('status') == 'archived']
    return sorted(archived, key=lambda x: x['archive_date'])
