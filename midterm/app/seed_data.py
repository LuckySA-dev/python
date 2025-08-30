from __future__ import annotations
from .models import Car, Customer
from .storage import CarRepo, CustomerRepo
from . import config

def seed_cars():
    repo = CarRepo()
    if len(repo) > 0: return
    examples = [
        (1001, "ABC-1234", "Toyota",  "Camry",   2021, 1500.00, 42850, 0, 1),
        (1002, "BCD-2345", "Honda",   "Civic",   2020, 1200.00, 61200, 1, 1),
        (1003, "CDE-3456", "Nissan",  "Almera",  2019,  900.00, 73210, 0, 1),
        (1004, "DEF-4567", "Mazda",   "2",       2022, 1300.00, 12000, 0, 1),
        (1005, "EFG-5678", "Toyota",  "Fortuner",2021, 2500.00, 30500, 1, 1),
        (1006, "FGH-6789", "BMW",     "530e",    2023, 3000.00,  8000, 1, 1),
        (1007, "GHI-7890", "Toyota",  "Yaris",   2018, 1100.00, 95000, 0, 1),
        (1008, "HIJ-8901", "Honda",   "Accord",  2022, 2400.00, 21000, 0, 1),
        (1009, "IJK-9012", "Mercedes","C300",    2021, 2900.00, 17000, 0, 1),
        (1010, "JKL-0123", "Nissan",  "March",   2017,  800.00,120000, 0, 0),
    ]
    for car_id, plate, brand, model, year, rate, odo, rented, active in examples:
        c = Car.new(car_id, plate, brand, model, year, rate, odo)
        c.is_rented = rented
        c.status = config.ACTIVE if active else config.DELETED
        repo.add(c)

def seed_customers():
    repo = CustomerRepo()
    if len(repo) > 0: return
    examples = [
        (2001, "Alice", "081-000-0001", "alice@example.com"),
        (2002, "Bob",   "081-000-0002", "bob@example.com"),
        (2003, "Carol", "081-000-0003", "carol@example.com"),
    ]
    for cid, name, phone, email in examples:
        repo.add(Customer.new(cid, name, phone, email))

def main():
    seed_cars(); seed_customers()
    print("Seeded (if empty).")

if __name__ == "__main__":
    main()
