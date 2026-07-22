# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: InvoicePad
APP_CONFIG = {
    "app_name": "InvoicePad",
    "version": 1,
    "currency_symbol": "₽",
    "default_due_days": 30,
    "max_invoices_per_client": None,
    "enable_notes": True,
}


def load_config(path=None):
    import json

    if path is None:
        return APP_CONFIG.copy()

    try:
        with open(path) as f:
            user = json.load(f)
        merged = {**APP_CONFIG, **user}
    except Exception:
        merged = APP_CONFIG.copy()
    return merged


def save_config(config):
    import json

    path = config.get("config_path") or "invoicepad_settings.json"
    with open(path, "w") as f:
        json.dump({k: v for k, v in config.items() if k != "config_path"}, f)
