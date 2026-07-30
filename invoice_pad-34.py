# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: InvoicePad
TEMPLATES = {
    "standard": {"amount": 100, "due_days": 7, "notes": ""},
    "premium": {"amount": 250, "due_days": 30, "notes": "Premium payment"},
}

def apply_template(template_name):
    if template_name not in TEMPLATES:
        print(f"Unknown template: {template_name}")
        return None
    t = dict(TEMPLATES[template_name])
    t["id"] = f"tmpl_{template_name}"
    return t
