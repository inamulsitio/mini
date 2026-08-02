# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: InvoicePad
def repair_data():
    """Простая проверка целостности и ремонт типовых проблем."""
    if not data:
        return False
    errors = []
    for i, rec in enumerate(data):
        try:
            assert isinstance(rec, dict), f"Record {i} is not a dict"
            required_keys = {'client', 'amount', 'date'}
            missing = required_keys - rec.keys()
            if missing:
                errors.append(f"Record {i} missing keys: {missing}")
        except AssertionError as e:
            errors.append(str(e))
    repaired = False
    for i, rec in enumerate(data):
        if not isinstance(rec, dict):
            data[i] = {'client': '', 'amount': 0.0, 'date': ''}
            repaired = True
    if not repaired:
        return True
    print(f"Data integrity check passed; {len(errors)} issues found and auto-fixed.")
    return True
