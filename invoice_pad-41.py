# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: InvoicePad
class DryRunContext:
    def __init__(self, client_id=None, invoice_id=None, payment_id=None, memo_id=None):
        self.client_id = client_id
        self.invoice_id = invoice_id
        self.payment_id = payment_id
        self.memo_id = memo_id
        self.changes = []
    
    def record(self, entity_type, id_field, value):
        self.changes.append({'type': entity_type, 'id': id_field, 'value': value})
    
    def __repr__(self):
        return f"DryRunContext({self.changes})"

def run_dry(client_id=None, invoice_id=None, payment_id=None, memo_id=None):
    ctx = DryRunContext(client_id, invoice_id, payment_id, memo_id)
    return ctx
