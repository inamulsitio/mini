# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: InvoicePad
import json, sys, os
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки в структуру проекта."""
    try:
        data = json.loads(json_string)
        
        # Валидация обязательных полей
        required_keys = ['clients', 'invoices']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Отсутствует обязательное поле '{key}'")
            
            if not isinstance(data[key], list):
                raise TypeError(f"Поле '{key}' должно быть списком")
        
        # Преобразование типов для клиентов
        processed_clients = []
        for client in data['clients']:
            if isinstance(client, dict):
                processed_clients.append({
                    'id': str(client.get('id', '')),
                    'name': str(client.get('name', '')),
                    'balance': float(client.get('balance', 0)) if isinstance(client.get('balance'), (int, float)) else 0.0,
                    'notes': client.get('notes', '') or '',
                    'status': client.get('status', 'active')
                })
            elif isinstance(client, str):
                # Парсинг строки "ID|Имя" если формат простой
                parts = client.split('|')
                processed_clients.append({
                    'id': parts[0] if len(parts) > 0 else '',
                    'name': parts[1] if len(parts) > 1 else '',
                    'balance': 0.0,
                    'notes': '',
                    'status': 'active'
                })
        
        # Преобразование типов для счетов
        processed_invoices = []
        for inv in data['invoices']:
            if isinstance(inv, dict):
                processed_invoices.append({
                    'id': str(inv.get('id', '')),
                    'client_id': str(inv.get('client_id', '')),
                    'amount': float(inv.get('amount', 0)) if isinstance(inv.get('amount'), (int, float)) else 0.0,
                    'due_date': inv.get('due_date', ''),
                    'status': inv.get('status', 'pending'),
                    'notes': inv.get('notes', '') or ''
                })
            elif isinstance(inv, str):
                # Парсинг строки "ID|ClientID|Сумма" если формат простой
                parts = inv.split('|')
                processed_invoices.append({
                    'id': parts[0] if len(parts) > 0 else '',
                    'client_id': parts[1] if len(parts) > 1 else '',
                    'amount': float(parts[2]) if len(parts) > 2 and parts[2].replace('.', '').isdigit() else 0.0,
                    'due_date': '',
                    'status': 'pending',
                    'notes': ''
                })
        
        return {
            'clients': processed_clients,
            'invoices': processed_invoices
        }

    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit
