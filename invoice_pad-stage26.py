# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: InvoicePad
import random, string

def demo_commands():
    print("=== Демо-команды InvoicePad ===\n")
    
    # Клиенты
    clients = [
        ("ООО Ромашка", "Москва"),
        ("ИП Иванов А.А.", "Санкт-Петербург"),
        ("Технопарк Лтд", "Новосибирск"),
        ("Стартап Вектор", "Екатеринбург"),
    ]
    
    for i, (name, city) in enumerate(clients):
        print(f"CREATE_CLIENT {i+1} {name} {city}")
    
    # Счета
    invoices = [
        ("Розничный магазин", 15000.0),
        ("Запчасти для ремонта", 8500.0),
        ("Консультационные услуги", 25000.0),
        ("Поставка оборудования", 42000.0),
    ]
    
    for i, (desc, amount) in enumerate(invoices):
        print(f"CREATE_INVOICE {i+1} {clients[i%len(clients)][0]} {desc} {amount:.2f}")
    
    # Оплатами
    payments = [
        ("Промышленное предприятие", 10000.0),
        ("Зарплата сотрудников", 5000.0),
        ("Аренда офиса", 30000.0),
        ("Супермаркет 'Вкусно'", 7500.0),
    ]
    
    for i, (desc, amount) in enumerate(payments):
        print(f"CREATE_PAYMENT {i+1} {clients[i%len(clients)][0]} {desc} {amount:.2f}")
    
    # Заметки
    notes = [
        "Оплатить до конца месяца",
        "Требует проверку качества",
        "Срочно, клиент ждёт",
        "Пересчитать НДС",
    ]
    
    for i, note in enumerate(notes):
        print(f"CREATE_NOTE {i+1} {note}")
    
    # Удаление
    print("DELETE_INVOICE 2")
    print("DELETE_PAYMENT 3")
    
    print("\n=== Демо-команды завершены ===")

demo_commands()
