from __future__ import annotations
from dataclasses import dataclass
import struct
from typing import ClassVar
from . import config

def _pack_str(s: str, size: int) -> bytes:
    b = (s or "").encode(config.ENCODING)[:size]
    return b + b"\x00" * (size - len(b))

def _unpack_str(b: bytes) -> str:
    return b.split(b"\x00", 1)[0].decode(config.ENCODING, errors="ignore").strip()

@dataclass
class Car:
    car_id: int
    status: int
    is_rented: int
    year: int
    daily_rate_thb: float
    odometer_km: int
    license_plate: str
    brand: str
    model: str
    created_at: int
    updated_at: int

    STRUCT_FMT: ClassVar[str] = config.CAR_STRUCT_FMT
    SIZE: ClassVar[int] = config.CAR_RECORD_SIZE

    def pack(self) -> bytes:
        return struct.pack(
            self.STRUCT_FMT,
            int(self.car_id),
            int(self.status),
            int(self.is_rented),
            int(self.year),
            float(self.daily_rate_thb),
            int(self.odometer_km),
            _pack_str(self.license_plate, config.CAR_PLATE_LEN),
            _pack_str(self.brand, config.CAR_BRAND_LEN),
            _pack_str(self.model, config.CAR_MODEL_LEN),
            int(self.created_at),
            int(self.updated_at),
        )

    @classmethod
    def unpack(cls, data: bytes) -> "Car":
        t = struct.unpack(cls.STRUCT_FMT, data)
        return cls(
            car_id=t[0], status=t[1], is_rented=t[2], year=t[3], daily_rate_thb=t[4],
            odometer_km=t[5], license_plate=_unpack_str(t[6]), brand=_unpack_str(t[7]),
            model=_unpack_str(t[8]), created_at=t[9], updated_at=t[10]
        )

    @classmethod
    def new(cls, car_id: int, license_plate: str, brand: str, model: str,
            year: int, rate: float, odo_km: int) -> "Car":
        ts = config.now_ts()
        return cls(
            car_id=car_id, status=config.ACTIVE, is_rented=0, year=year,
            daily_rate_thb=rate, odometer_km=odo_km, license_plate=license_plate,
            brand=brand, model=model, created_at=ts, updated_at=ts
        )

@dataclass
class Customer:
    customer_id: int
    status: int
    name: str
    phone: str
    email: str
    created_at: int
    updated_at: int

    STRUCT_FMT: ClassVar[str] = config.CUSTOMER_STRUCT_FMT
    SIZE: ClassVar[int] = config.CUSTOMER_RECORD_SIZE

    def pack(self) -> bytes:
        return struct.pack(
            self.STRUCT_FMT,
            int(self.customer_id), int(self.status),
            _pack_str(self.name, config.CUST_NAME_LEN),
            _pack_str(self.phone, config.CUST_PHONE_LEN),
            _pack_str(self.email, config.CUST_EMAIL_LEN),
            int(self.created_at), int(self.updated_at)
        )

    @classmethod
    def unpack(cls, data: bytes) -> "Customer":
        t = struct.unpack(cls.STRUCT_FMT, data)
        return cls(
            customer_id=t[0], status=t[1],
            name=_unpack_str(t[2]), phone=_unpack_str(t[3]), email=_unpack_str(t[4]),
            created_at=t[5], updated_at=t[6]
        )

    @classmethod
    def new(cls, customer_id: int, name: str, phone: str, email: str) -> "Customer":
        ts = config.now_ts()
        return cls(customer_id=customer_id, status=config.ACTIVE, name=name,
                   phone=phone, email=email, created_at=ts, updated_at=ts)

@dataclass
class Rental:
    rental_id: int
    status: int
    car_id: int
    customer_id: int
    start_ts: int
    end_ts: int  # 0 if open
    daily_rate_thb: float
    total_days: int
    total_cost_thb: float
    created_at: int
    updated_at: int

    STRUCT_FMT: ClassVar[str] = config.RENTAL_STRUCT_FMT
    SIZE: ClassVar[int] = config.RENTAL_RECORD_SIZE

    def pack(self) -> bytes:
        return struct.pack(
            self.STRUCT_FMT,
            int(self.rental_id), int(self.status),
            int(self.car_id), int(self.customer_id),
            int(self.start_ts), int(self.end_ts),
            float(self.daily_rate_thb), int(self.total_days),
            float(self.total_cost_thb),
            int(self.created_at), int(self.updated_at)
        )

    @classmethod
    def unpack(cls, data: bytes) -> "Rental":
        t = struct.unpack(cls.STRUCT_FMT, data)
        return cls(
            rental_id=t[0], status=t[1], car_id=t[2], customer_id=t[3],
            start_ts=t[4], end_ts=t[5], daily_rate_thb=t[6],
            total_days=t[7], total_cost_thb=t[8], created_at=t[9], updated_at=t[10]
        )

    @classmethod
    def open(cls, rental_id: int, car_id: int, customer_id: int, rate: float) -> "Rental":
        ts = config.now_ts()
        return cls(
            rental_id=rental_id, status=config.ACTIVE, car_id=car_id, customer_id=customer_id,
            start_ts=ts, end_ts=0, daily_rate_thb=rate, total_days=0, total_cost_thb=0.0,
            created_at=ts, updated_at=ts
        )

    def close(self, end_ts: int | None = None) -> None:
        if self.end_ts != 0:
            return
        end_ts = end_ts or config.now_ts()
        days = max(1, int((end_ts - self.start_ts) // 86400))
        self.end_ts = end_ts
        self.total_days = days
        self.total_cost_thb = round(days * float(self.daily_rate_thb), 2)
        self.updated_at = config.now_ts()
