# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: InvoicePad
import json, os


def load_profiles():
    path = "profiles.json"
    if not os.path.exists(path):
        return [{"id": 1, "name": "Администратор", "role": "admin", "notes": ""}]
    with open(path) as f:
        data = json.load(f)
    default = {"id": 1, "name": "Администратор", "role": "admin", "notes": ""}
    if not any(p.get("id") == default["id"] for p in data):
        return [default] + data
    return data


def save_profiles(profiles):
    with open("profiles.json", "w") as f:
        json.dump(profiles, f, indent=2)
