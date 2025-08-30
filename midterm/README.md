# Car Rent System (struct + fixed-length, OOP, multi-file)

**Standard Library only** — Python 3.10+

## Layout
```
car_rent_struct_oop/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── storage.py
│   ├── validators.py
│   ├── report.py
│   ├── menu.py
│   ├── main.py
│   └── seed_data.py
└── data/
    └── (created on first run)
```

## Run
```bash
python -m app.seed_data   # (1) Seed example rows
python -m app.main        # (2) Start the CLI
# or generate report directly
python -c "from app.report import generate_report; print(generate_report())"
```
