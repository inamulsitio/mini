# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: InvoicePad
import json
from datetime import datetime, timedelta
from pathlib import Path

# Конфигурация и точка входа
APP_NAME = "InvoicePad"
DATA_FILE = "data.json"

def load_data():
    """Загрузка данных из JSON файла или создание пустой структуры."""
    path = Path(DATA_FILE)
    if not path.exists():
        return {
            "clients": [],
            "invoices": [],
            "payments": []
        }
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"clients": [], "invoices": [], "payments": []}

def save_data(data):
    """Сохранение данных в JSON файл."""
    path = Path(DATA_FILE)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Демонстрационные данные
def init_demo_data():
    data = load_data()
    
    # Добавление демо-клиента
    if not any(c["name"] == "ООО 'Вектор'" for c in data["clients"]):
        client = {
            "id": 1,
            "name": "ООО 'Вектор'",
            "balance": 0.0,
            "notes": "Поставщик оборудования"
        }
        data["clients"].append(client)

    # Добавление демо-счета
    if not any(inv["invoice_id"] == "INV-2023-001" for inv in data["invoices"]):
        invoice = {
            "invoice_id": "INV-2023-001",
            "client_id": 1,
            "amount": 15000.00,
            "due_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
            "status": "pending", # pending, paid, overdue
            "notes": "Закупка серверов"
        }
        data["invoices"].append(invoice)

    # Сохранение начальных данных
    save_data(data)
    return data
