# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: InvoicePad
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [Invoice.from_dict(item) for item in data]
        elif isinstance(data, dict):
            return [Invoice.from_dict(data)]
        else:
            print("Ошибка: некорректный формат JSON")
            return []
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка при загрузке: {e}")
        return []
