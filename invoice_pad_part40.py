# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: InvoicePad
import argparse

def main():
    parser = argparse.ArgumentParser(description="InvoicePad CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("add", help="Добавить запись")
    p.add_argument("kind", choices=["invoice", "payment"], help="Тип записи")
    p.add_argument("--client", required=True, help="Клиент")
    p.add_argument("--amount", required=True, type=float, help="Сумма")
    p.add_argument("--note", default="", help="Заметка")
    sub.add_parser("list", help="Показать все")
    sub.add_parser("show", help="Показать по ID")
    sub.add_parser("delete", help="Удалить по ID")
    args = parser.parse_args()
    print(f"Command: {args.command}, kind: {args.kind if hasattr(args, 'kind') else 'N/A'}")
