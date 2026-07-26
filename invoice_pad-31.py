# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: InvoicePad
def switch_profile():
    """Переключение активного профиля: выбор из сохранённых, создание нового."""
    from datetime import datetime

    def _prompt(msg):
        return input(f"{msg}: ").strip() or ""

    profiles = get_profiles()  # предполагаемый импорт существующей функции
    if not profiles:
        print("Нет сохранённых профилей.")
        return

    print("\n=== Профили ===")
    for i, (name, data) in enumerate(profiles, 1):
        active_mark = " ★" if name == active_profile_name else ""
        print(f"  {i}. [{active_mark}] {name}")

    choice = _prompt("Введите номер профиля или 'n' для нового")
    if choice.lower() == "n":
        new_name = _prompt("Имя нового профиля")
        if not new_name:
            return
        profiles.append({
            "name": new_name,
            "email": "",
            "phone": "",
            "notes": "",
            "created_at": datetime.now().isoformat(),
        })
    else:
        idx = int(choice) - 1
        if idx < len(profiles):
            profiles[idx]["active"] = True

    save_profiles(profiles)
    active_profile_name = get_active_profile_name() or ""
    print(f"\nАктивный профиль: {profiles[0]['name'] if profiles else '—'}")
