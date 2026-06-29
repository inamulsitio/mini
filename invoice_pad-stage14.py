# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: InvoicePad
def generate_summary(invoices, payments):
    clients = {}
    for inv in invoices:
        cid = inv['client_id']
        if cid not in clients:
            clients[cid] = {'name': inv.get('client_name', 'Unknown'), 'total_due': 0}
        clients[cid]['total_due'] += inv['amount'] - sum(p for p in payments if p['invoice_id'] == inv['id'])

    overdue = [inv for inv in invoices if (inv['due_date'] or '') and inv['status'] != 'paid' and inv['due_date'] < str(datetime.now().date())]
    
    print(f"=== Сводка по счетам ({len(invoices)} всего) ===")
    print(f"Всего клиентов: {len(clients)}")
    for cid, data in sorted(clients.items()):
        status = "Просрочено!" if any(inv['id'] == inv_id and (inv['due_date'] or '') < str(datetime.now().date()) for inv_id, inv in [(i['client_id'], i) for i in invoices]) else "В порядке"
        print(f"{data['name']} ({cid}): {data['total_due']:,.2f} руб. [{status}]")
    if overdue:
        print(f"\n⚠ Просрочено счетов: {len(overdue)}")
