# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: InvoicePad
def parse_date(date_str):
    """Разбирает строку даты в формате ДД.ММ.ГГГГ, возвращает datetime.date или None."""
    if not date_str:
        return None
    try:
        parts = date_str.strip().split('.')
        if len(parts) != 3:
            raise ValueError("Дата должна быть в формате ДД.ММ.ГГГГ")
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        return datetime.date(year, month, day)
    except (ValueError, TypeError):
        return None

def error_to_message(err):
    """Преобразует исключение в понятное сообщение."""
    msg = str(err).strip().lower() if err else "Неизвестная ошибка"
    if 'invalid date' in msg or 'неверная дата' in msg:
        return "Некорректный формат даты. Используйте ДД.ММ.ГГГГ."
    if 'not a number' in msg or 'value error' in msg:
        return "Введите корректное число."
    if 'empty' in msg:
        return "Поле не может быть пустым."
    return f"Произошла ошибка: {err}"
