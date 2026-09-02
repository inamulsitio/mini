# === Stage 43: Добавь пагинацию длинных списков ===
# Project: InvoicePad
def paginate(items, page_size=10, current_page=1):
    total_pages = max(1, (len(items) + page_size - 1) // page_size)
    current_page = max(1, min(current_page, total_pages))
    start = (current_page - 1) * page_size
    end = start + page_size
    page_items = items[start:end]
    return {
        "items": page_items,
        "current_page": current_page,
        "total_pages": total_pages,
        "total_items": len(items),
        "has_next": current_page < total_pages,
        "has_prev": current_page > 1,
    }
