# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: InvoicePad
def next_action_suggestions():
    """Return a list of actionable recommendations based on current invoice state."""
    actions = []
    
    if not invoices:
        return ["Create your first invoice to get started."]
    
    overdue_count = sum(1 for inv in invoices if inv['due_date'] and (datetime.now() - datetime.fromisoformat(inv['due_date'])).days > 7)
    if overdue_count:
        actions.append(f"Follow up with {overdue_count} client(s) whose invoices are past due.")
    
    pending_invoices = [inv for inv in invoices if inv.get('status') not in ['paid', 'cancelled']]
    if pending_invoices and datetime.now() - datetime.fromisoformat(pending_invoices[0].get('created_date')) > 3:
        actions.append("Review pending invoices older than 3 days to confirm or chase payment.")
    
    if any(inv['total'] == inv.get('paid', 0) for inv in invoices if inv.get('status') != 'paid'):
        actions.append("Mark fully paid invoices as completed and update client records.")
    
    clients_without_invoices = [c for c in clients if not any(i['client_id'] == c['id'] for i in invoices)]
    if clients_without_invoices:
        actions.append(f"Consider sending a new invoice to {len(clients_without_invoices)} inactive client(s).")
    
    return actions if actions else ["All current invoices are up-to-date. Consider creating a new one."]
