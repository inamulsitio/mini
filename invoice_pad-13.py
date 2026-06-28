# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: InvoicePad
def search_clients(query):
    if not query:
        return []
    q = query.lower().strip()
    results = []
    for client in clients_data:
        fields_to_check = [client['name'], client['email']]
        if any(q in str(f).lower() for f in fields_to_check):
            results.append(client)
    return results
