# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: InvoicePad
def check_overdue_reminders(self):
        """Проверяет просроченные напоминания по срокам оплаты."""
        today = datetime.date.today()
        for invoice in self.invoices:
            if not invoice.is_paid and invoice.due_date < today:
                days_overdue = (today - invoice.due_date).days
                reminder = f"Счёт #{invoice.id} просрочен на {days_overdue} дн."
                print(f"[НАПОМИНАНИЕ] {reminder}")
