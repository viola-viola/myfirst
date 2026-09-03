# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: TravelLedger
TEMPLATE_STORE = {}

def register_template(name, fields, default=None):
    TEMPLATE_STORE[name] = {'fields': fields, 'default': default or {}}

def create_from_template(name, **overrides):
    if name not in TEMPLATE_STORE:
        raise KeyError(f"Template '{name}' not found. Available: {list(TEMPLATE_STORE.keys())}")
    tpl = TEMPLATE_STORE[name]
    record = dict(tpl['default'])
    for f in tpl['fields']:
        record.setdefault(f)
    record.update(overrides)
    return record
