# === Stage 17: Добавь группировку записей по категориям ===
# Project: InvoicePad
def group_by_category(records):
    groups = {}
    for rec in records:
        cat = rec.get('category', 'general')
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(rec)
    return dict(sorted(groups.items()))
