# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: InvoicePad
def main():
    while True:
        print("\n=== InvoicePad ===")
        print("1. Добавить клиента")
        print("2. Создать счёт")
        print("3. Записать оплату")
        print("4. Просмотреть все данные")
        print("5. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            name = input("Имя клиента: ")
            notes = input("Заметки (опционально): ") or ""
            clients[name] = {"notes": notes}
            print(f"Клиент {name} добавлен.")
        elif choice == "2":
            client_name = input("Имя клиента: ")
            if client_name not in clients:
                print("Ошибка: Клиент не найден.")
                continue
            amount_str = input("Сумма (руб): ")
            try:
                amount = float(amount_str)
            except ValueError:
                print("Некорректная сумма.")
                continue
            due_date = input("Дата оплаты (ДД.ММ.ГГГГ): ") or ""
            invoice_id = len(invoices) + 1000
            invoices[invoice_id] = {"client": client_name, "amount": amount, "due_date": due_date}
            print(f"Счёт #{invoice_id} создан.")
        elif choice == "3":
            invoice_id_str = input("ID счёта для оплаты: ")
            try:
                invoice_id = int(invoice_id_str)
            except ValueError:
                print("Некорректный ID счёта.")
                continue
            if invoice_id in invoices and not invoices[invoice_id].get("paid"):
                amount_paid = float(input("Сумма оплаты: "))
                invoices[invoice_id]["amount"] -= amount_paid
                invoices[invoice_id]["paid"] = True
                print(f"Оплата #{invoice_id} обновлена.")
            else:
                print("Ошибка: Счёт не найден или уже оплачен полностью.")
        elif choice == "4":
            if not clients and not invoices:
                print("База данных пуста.")
            else:
                for cid, cdata in sorted(clients.items()):
                    print(f"\n--- Клиент: {cid} ---")
                    print(f"Заметки: {cdata['notes']}")
                for inv_id, inv_data in sorted(invoices.items(), key=lambda x: int(x[0])):
                    status = "Оплачен" if inv_data.get("paid") else f"До оплаты: {inv_data['amount']}"
                    print(f"\n--- Счёт #{inv_id} ({inv_data['client']}) ---")
                    print(f"Сумма: {inv_data['amount']} руб., Срок: {inv_data['due_date']}, Статус: {status}")
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    clients = {}
    invoices = {}
    main()
