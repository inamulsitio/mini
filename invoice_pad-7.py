# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: InvoicePad
def sort_records(records, key='date', reverse=False):
    if not records: return []
    order_map = {'urgent': 0, 'high': 1, 'medium': 2, 'low': 3}
    def get_sort_key(item):
        try:
            val = item[key]
            if key == 'priority': return order_map.get(val.lower(), 4)
            if isinstance(val, str): return (0, len(val), val)
            return (1, -val, '')
        except Exception: return (2, '', '')
    sorted_records = sorted(records, key=get_sort_key, reverse=reverse)
    return sorted_records
