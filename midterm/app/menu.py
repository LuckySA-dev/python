from __future__ import annotations
from . import config, validators
from .models import Car, Customer, Rental
from .storage import CarRepo, CustomerRepo, RentalRepo
from .report import generate_report

def _prompt_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("Please enter an integer.")

def _prompt_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg).strip())
        except ValueError:
            print("Please enter a number.")

def car_menu():
    repo = CarRepo()
    while True:
        print("\n[Car Menu]")
        print("1) Add  2) Update  3) Delete  4) View All  5) View by ID  6) Back")
        ch = input("Select: ").strip()
        if ch == "1":
            car_id = _prompt_int("car_id: ")
            plate = input("license_plate (ABC-1234): ").strip().upper()
            if not validators.valid_plate(plate):
                print("Invalid plate pattern."); continue
            brand = validators.clamp_str(input("brand: "), 12)
            model = validators.clamp_str(input("model: "), 16)
            year = _prompt_int("year: ")
            if not validators.valid_year(year):
                print("Invalid year."); continue
            rate = _prompt_float("daily_rate_thb: ")
            if not validators.valid_rate(rate):
                print("Invalid rate."); continue
            odo = _prompt_int("odometer_km: ")
            rec = Car.new(car_id, plate, brand, model, year, rate, odo)
            try:
                repo.add(rec); print("Added.")
            except Exception as e:
                print("Error:", e)
        elif ch == "2":
            car_id = _prompt_int("car_id to update: ")
            idx, rec = repo.find_by_id(car_id)
            if rec is None: print("Not found."); continue
            plate = input(f"license_plate [{rec.license_plate}]: ").strip() or rec.license_plate
            if not validators.valid_plate(plate):
                print("Invalid plate."); continue
            brand = input(f"brand [{rec.brand}]: ").strip() or rec.brand
            model = input(f"model [{rec.model}]: ").strip() or rec.model
            year_s = input(f"year [{rec.year}]: ").strip() or str(rec.year)
            rate_s = input(f"daily_rate_thb [{rec.daily_rate_thb}]: ").strip() or str(rec.daily_rate_thb)
            odo_s = input(f"odometer_km [{rec.odometer_km}]: ").strip() or str(rec.odometer_km)
            try:
                rec.license_plate = validators.clamp_str(plate, 12)
                rec.brand = validators.clamp_str(brand, 12)
                rec.model = validators.clamp_str(model, 16)
                rec.year = int(year_s); rec.daily_rate_thb = float(rate_s); rec.odometer_km = int(odo_s)
                rec.updated_at = config.now_ts()
                repo.write_at(idx, rec); print("Updated.")
            except Exception as e:
                print("Error:", e)
        elif ch == "3":
            car_id = _prompt_int("car_id to delete: ")
            print("Deleted (soft)." if repo.soft_delete(car_id) else "Not found or already deleted.")
        elif ch == "4":
            for _, r in repo.iter_all():
                print(f"{r.car_id} {r.license_plate} {r.brand} {r.model} {r.year} rate={r.daily_rate_thb:.2f} status={r.status} rented={r.is_rented}")
        elif ch == "5":
            car_id = _prompt_int("car_id: ")
            print(repo.find_by_id(car_id)[1] or "Not found.")
        elif ch == "6":
            return
        else:
            print("Invalid choice.")

def customer_menu():
    repo = CustomerRepo()
    while True:
        print("\n[Customer Menu]")
        print("1) Add  2) Update  3) Delete  4) View All  5) View by ID  6) Back")
        ch = input("Select: ").strip()
        if ch == "1":
            cid = _prompt_int("customer_id: ")
            name = input("name: ").strip()
            phone = input("phone: ").strip()
            email = input("email: ").strip()
            repo.add(Customer.new(cid, name, phone, email)); print("Added.")
        elif ch == "2":
            cid = _prompt_int("customer_id to update: ")
            idx, rec = repo.find_by_id(cid)
            if rec is None: print("Not found."); continue
            name = input(f"name [{rec.name}]: ").strip() or rec.name
            phone = input(f"phone [{rec.phone}]: ").strip() or rec.phone
            email = input(f"email [{rec.email}]: ").strip() or rec.email
            rec.name, rec.phone, rec.email = name, phone, email
            rec.updated_at = config.now_ts()
            repo.write_at(idx, rec); print("Updated.")
        elif ch == "3":
            cid = _prompt_int("customer_id to delete: ")
            print("Deleted." if repo.soft_delete(cid) else "Not found or already deleted.")
        elif ch == "4":
            for _, r in repo.iter_all(): print(r)
        elif ch == "5":
            cid = _prompt_int("customer_id: ")
            print(repo.find_by_id(cid)[1] or "Not found.")
        elif ch == "6":
            return
        else:
            print("Invalid choice.")

def rental_menu():
    cars, cust, rent = CarRepo(), CustomerRepo(), RentalRepo()
    while True:
        print("\n[Rental Menu]")
        print("1) Open Rental  2) Close Rental  3) View All  4) Back")
        ch = input("Select: ").strip()
        if ch == "1":
            rid = _prompt_int("rental_id: ")
            car_id = _prompt_int("car_id: ")
            customer_id = _prompt_int("customer_id: ")
            _, car = cars.find_by_id(car_id)
            if not car or car.status != config.ACTIVE:
                print("Car not available."); continue
            if car.is_rented: print("Car already rented."); continue
            if not cust.find_by_id(customer_id)[1]: print("Customer not found."); continue
            rec = Rental.open(rid, car_id, customer_id, car.daily_rate_thb)
            rent.add(rec)
            idx, car2 = cars.find_by_id(car_id)
            car2.is_rented = 1; car2.updated_at = config.now_ts()
            cars.write_at(idx, car2)
            print("Rental opened.")
        elif ch == "2":
            rid = _prompt_int("rental_id: ")
            idx, r = rent.find_by_id(rid)
            if not r or r.end_ts != 0: print("Not found or already closed."); continue
            r.close(); rent.write_at(idx, r)
            idxc, car = cars.find_by_id(r.car_id)
            if car: car.is_rented = 0; car.updated_at = config.now_ts(); cars.write_at(idxc, car)
            print(f"Rental closed. Total {r.total_days} day(s), cost {r.total_cost_thb:.2f} THB.")
        elif ch == "3":
            for _, r in rent.iter_all(): print(r)
        elif ch == "4":
            return
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("\n==== Car Rent System (struct + fixed-length) ====")
        print("1) Cars  2) Customers  3) Rentals  4) Generate Report  0) Exit")
        ch = input("Select: ").strip()
        if ch == "1": car_menu()
        elif ch == "2": customer_menu()
        elif ch == "3": rental_menu()
        elif ch == "4":
            path = generate_report(); print("Report generated at:", path)
        elif ch == "0":
            print("Bye."); return
        else: print("Invalid choice.")
