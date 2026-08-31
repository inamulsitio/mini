# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: InvoicePad
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"

    @staticmethod
    def disable():
        import os
        os.environ["NO_COLOR"] = "1"
        return Color

    @staticmethod
    def enabled():
        return Color

    @staticmethod
    def text(text, code=""):
        if code:
            return f"{code}{text}{Color.RESET}"
        return text
