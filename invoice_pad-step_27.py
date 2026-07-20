# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: InvoicePad
import random, datetime, json

def reset_demo_data():
    """Генерирует ~15 случайных счетов для быстрого старта."""
    names = [f"Клиент {i}" for i in range(1, 20)]
    notes = ["Оплата по договору", "Рекламация", "Срочный заказ", "Без оплаты"]
    clients = [random.choice(names) for _ in range(random.randint(8, 12))]
    invoices = []
    for i in range(15):
        inv = {
            "id": f"INV-{i+1:03d}",
            "client": random.choice(clients),
            "amount": round(random.uniform(1000, 50000), 2),
            "due_date": (datetime.date.today() + datetime.timedelta(days=random.randint(7, 90))).isoformat(),
            "notes": random.choice(notes),
            "status": random.choice(["pending", "paid", "overdue"]),
        }
        invoices.append(inv)
    return {"clients": clients, "invoices": invoices}

def clear_state():
    """Полностью очищает все данные приложения."""
    data = {}
    with open("data.json", "w") as f:
        json.dump(data, f)
    return data
