# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: InvoicePad
def calculate_weekly_stats(records):
    from datetime import date, timedelta
    stats = {}
    today = date.today()
    for i in range(52):
        week_start = (today - timedelta(days=today.weekday())).replace(day=1) + timedelta(days=i*7)
        week_end = week_start + timedelta(days=6)
        key = f"Week {week_start.isocalendar()[0]}W{week_start.isocalendar()[1]:02d}"
        total_amount = 0.0
        paid_count = 0
        overdue_count = 0
        for rec in records:
            if week_start <= rec['date'] <= week_end:
                total_amount += rec['amount']
                if rec.get('paid'):
                    paid_count += 1
                elif rec.get('due_date') and rec['due_date'] < rec['date']:
                    overdue_count += 1
        stats[key] = {'total': round(total_amount, 2), 'paid': paid_count, 'overdue': overdue_count}
    return stats
