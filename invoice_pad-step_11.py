# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: InvoicePad
import json, os

DATA_FILE = "invoices.json"

def save_to_file(invoices):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(invoices, f, ensure_ascii=False, indent=2)

def load_from_file():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('invoices', [])
    except (json.JSONDecodeError, IOError):
        return []

def init_storage():
    if not os.path.exists(DATA_FILE):
        save_to_file({'invoices': [], 'clients': {}})
