# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: InvoicePad
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "exported_at": datetime.now().isoformat(),
        "clients": clients,
        "invoices": invoices,
        "payments": payments,
        "notes": notes
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
