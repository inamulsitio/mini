# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: InvoicePad
class TagManager:
    def __init__(self, db):
        self.db = db
    
    def add_tag(self, tag_name):
        if not any(t['name'] == tag_name for t in self.db.get('tags', [])):
            self.db.setdefault('tags', []).append({'id': len(self.db.get('tags', [])) + 1, 'name': tag_name})
    
    def remove_tag(self, tag_name):
        tags = [t for t in self.db.get('tags', []) if t['name'] != tag_name]
        return len(tags) < len(self.db.get('tags', []))
    
    def assign_tags_to_invoice(self, invoice_id, tag_names):
        invoices = self.db.setdefault('invoices', [])
        for inv in invoices:
            if inv['id'] == invoice_id:
                existing_ids = {t['name']: t['id'] for t in self.db.get('tags', [])}
                new_tags = []
                removed_names = set()
                for name in tag_names:
                    if name in existing_ids and not any(t['invoiceId'] == invoice_id and t['tagName'] == name for t in inv.get('tags', [])):
                        inv.setdefault('tags', []).append({'id': existing_ids[name], 'tagName': name, 'invoiceId': invoice_id})
                    elif name not in existing_ids:
                        new_tags.append(name)
                if new_tags:
                    self.db.setdefault('tags', []).extend([{'id': len(self.db.get('tags', [])) + 1, 'name': n} for n in new_tags])
                removed_names = set(tag_names) - {t['tagName'] for t in inv.get('tags', [])}
                return True if removed_names else False
