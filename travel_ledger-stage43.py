# === Stage 43: Добавь пагинацию длинных списков ===
# Project: TravelLedger
class Pagination:
    def __init__(self, data, page_size=10):
        self.data = data
        self.page_size = page_size
        self.total_pages = (len(data) + page_size - 1) // page_size
        self.current_page = 1

    def get_page(self):
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        return {
            "items": self.data[start:end],
            "current_page": self.current_page,
            "total_pages": self.total_pages,
            "has_next": self.current_page < self.total_pages,
            "has_prev": self.current_page > 1,
        }

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            return self.get_page()
        return None

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            return self.get_page()
        return None
