# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: InvoicePad
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status is not None and record['status'] != status:
            continue
        if category is not None and record.get('category') != category:
            continue
        if tags is not None and not any(tag.lower() in (record.get('tags', []) or '').lower() for tag in tags):
            continue
        filtered.append(record)
    return filtered
