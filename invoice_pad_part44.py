# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: InvoicePad
import shutil
import os
from datetime import datetime


def backup_data_file(data_path: str, backup_dir: str = "backups") -> str:
    """Сохранить резервную копию файла данных."""
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}_{os.path.basename(data_path)}")
    shutil.copy2(data_path, backup_path)
    return backup_path
