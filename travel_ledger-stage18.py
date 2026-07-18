# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: TravelLedger
def add_tag(item, tag):
    if item.tags is None:
        item.tags = set()
    item.tags.add(tag)
    return item

def remove_tag(item, tag):
    if item.tags and tag in item.tags:
        item.tags.discard(tag)
    return item
