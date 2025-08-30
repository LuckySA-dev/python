from __future__ import annotations
import os
from typing import Type, Iterable, Tuple, Optional, Any, Dict
from . import config
from .models import Car, Customer, Rental

Record = Any

class BinaryTable:
    """Fixed-length struct-based binary file table (append/read/update/soft-delete)."""
    def __init__(self, path: str, record_cls: Type[Record]):
        self.path = path
        self.record_cls = record_cls
        self.struct_fmt = record_cls.STRUCT_FMT
        self.rec_size = record_cls.SIZE
        config.ensure_data_dirs()
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, "wb") as _:
                pass

    def _open(self, mode: str = "rb+"):
        return open(self.path, mode)

    def __len__(self) -> int:
        if not os.path.exists(self.path):
            return 0
        return os.path.getsize(self.path) // self.rec_size

    def read_at(self, index: int) -> Optional[Record]:
        with self._open("rb") as f:
            f.seek(index * self.rec_size)
            data = f.read(self.rec_size)
            if len(data) != self.rec_size:
                return None
            return self.record_cls.unpack(data)

    def write_at(self, index: int, rec: Record) -> None:
        data = rec.pack()
        if len(data) != self.rec_size:
            raise ValueError("Packed record size mismatch")
        with self._open("rb+") as f:
            f.seek(index * self.rec_size)
            f.write(data); f.flush()

    def append(self, rec: Record) -> int:
        data = rec.pack()
        if len(data) != self.rec_size:
            raise ValueError("Packed record size mismatch")
        with self._open("ab") as f:
            f.write(data); f.flush()
        return len(self) - 1

    def iter_all(self) -> Iterable[Tuple[int, Record]]:
        count = len(self)
        with self._open("rb") as f:
            for idx in range(count):
                f.seek(idx * self.rec_size)
                data = f.read(self.rec_size)
                if len(data) != self.rec_size:
                    break
                yield idx, self.record_cls.unpack(data)

    def build_index(self, key_attr: str = "car_id") -> Dict[int, int]:
        index: Dict[int, int] = {}
        for idx, rec in self.iter_all():
            key = getattr(rec, key_attr)
            index[int(key)] = idx
        return index

class CarRepo(BinaryTable):
    def __init__(self): super().__init__(config.CARS_FILE, Car)

    def find_by_id(self, car_id: int):
        for idx, rec in self.iter_all():
            if rec.car_id == int(car_id):
                return idx, rec
        return None, None

    def add(self, car: Car) -> int:
        idx, _ = self.find_by_id(car.car_id)
        if idx is not None:
            raise ValueError(f"car_id {car.car_id} already exists")
        return super().append(car)

    def soft_delete(self, car_id: int) -> bool:
        idx, rec = self.find_by_id(car_id)
        if idx is None or rec.status == config.DELETED:
            return False
        rec.status = config.DELETED
        rec.is_rented = 0
        rec.updated_at = config.now_ts()
        self.write_at(idx, rec)
        return True

class CustomerRepo(BinaryTable):
    def __init__(self): super().__init__(config.CUSTOMERS_FILE, Customer)

    def find_by_id(self, customer_id: int):
        for idx, rec in self.iter_all():
            if rec.customer_id == int(customer_id):
                return idx, rec
        return None, None

    def add(self, customer: Customer) -> int:
        idx, _ = self.find_by_id(customer.customer_id)
        if idx is not None:
            raise ValueError(f"customer_id {customer.customer_id} already exists")
        return super().append(customer)

    def soft_delete(self, customer_id: int) -> bool:
        idx, rec = self.find_by_id(customer_id)
        if idx is None or rec.status == config.DELETED:
            return False
        rec.status = config.DELETED
        rec.updated_at = config.now_ts()
        self.write_at(idx, rec)
        return True

class RentalRepo(BinaryTable):
    def __init__(self): super().__init__(config.RENTALS_FILE, Rental)

    def find_by_id(self, rental_id: int):
        for idx, rec in self.iter_all():
            if rec.rental_id == int(rental_id):
                return idx, rec
        return None, None

    def add(self, rental: Rental) -> int:
        idx, _ = self.find_by_id(rental.rental_id)
        if idx is not None:
            raise ValueError(f"rental_id {rental.rental_id} already exists")
        return super().append(rental)

    def close_rental(self, rental_id: int) -> bool:
        idx, rec = self.find_by_id(rental_id)
        if idx is None or rec.end_ts != 0:
            return False
        rec.close()
        self.write_at(idx, rec)
        return True
