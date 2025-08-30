"""
Configuration for the Car Rent System (struct + fixed-length records).
Only Python Standard Library is used.
"""
from __future__ import annotations
import os

APP_VERSION = "1.0"
ENDIANNESS = "<"  # Little-endian
ENCODING = "utf-8"

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORT_PATH = os.path.join(DATA_DIR, "report.txt")

# ---------- Car table (cars.dat) ----------
CAR_PLATE_LEN = 12
CAR_BRAND_LEN = 12
CAR_MODEL_LEN = 16

# struct format: I I I I f I 12s 12s 16s I I  => total 72 bytes
CAR_STRUCT_FMT = (
    f"{ENDIANNESS}"
    "I" # car_id
    "I" # status (1=Active,0=Deleted)
    "I" # is_rented (1/0)
    "I" # year
    "f" # daily_rate_thb
    "I" # odometer_km
    f"{CAR_PLATE_LEN}s" # license_plate
    f"{CAR_BRAND_LEN}s" # brand
    f"{CAR_MODEL_LEN}s" # model
    "I" # created_at (unix ts)
    "I" # updated_at (unix ts)
)
CAR_RECORD_SIZE = 72
CARS_FILE = os.path.join(DATA_DIR, "cars.dat")

# ---------- Customer table (customers.dat) ----------
CUST_NAME_LEN = 32
CUST_PHONE_LEN = 16
CUST_EMAIL_LEN = 32

CUSTOMER_STRUCT_FMT = (
    f"{ENDIANNESS}"
    "I" # customer_id
    "I" # status
    f"{CUST_NAME_LEN}s"
    f"{CUST_PHONE_LEN}s"
    f"{CUST_EMAIL_LEN}s"
    "I" # created_at
    "I" # updated_at
)
CUSTOMER_RECORD_SIZE = 4+4+CUST_NAME_LEN+CUST_PHONE_LEN+CUST_EMAIL_LEN+4+4
CUSTOMERS_FILE = os.path.join(DATA_DIR, "customers.dat")

# ---------- Rental table (rentals.dat) ----------
RENTAL_STRUCT_FMT = (
    f"{ENDIANNESS}"
    "I" # rental_id
    "I" # status
    "I" # car_id
    "I" # customer_id
    "I" # start_ts
    "I" # end_ts (0 if open)
    "f" # daily_rate_thb (snapshot)
    "I" # total_days
    "f" # total_cost_thb
    "I" # created_at
    "I" # updated_at
)
RENTAL_RECORD_SIZE = 4*9 + 4 + 4  # ints: 9*4, floats: 2*4 = 44
RENTALS_FILE = os.path.join(DATA_DIR, "rentals.dat")

ACTIVE = 1
DELETED = 0

def ensure_data_dirs() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)

def now_ts() -> int:
    import time
    return int(time.time())
