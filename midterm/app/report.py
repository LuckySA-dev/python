from __future__ import annotations
from typing import List, Dict
from . import config
from .storage import CarRepo
from datetime import datetime
import statistics

def _fmt_yesno(b: int) -> str:
    return "Yes" if int(b) else "No"

def _status(st: int) -> str:
    return "Active" if int(st) == config.ACTIVE else "Deleted"

def generate_report(path: str | None = None) -> str:
    path = path or config.REPORT_PATH
    repo = CarRepo()
    rows = [rec for _, rec in repo.iter_all()]

    lines: List[str] = []
    tz = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S (%z)")
    lines.append("Car Rent System — Summary Report (Sample)")
    lines.append(f"Generated At : {tz}")
    lines.append(f"App Version  : {config.APP_VERSION}")
    lines.append(f"Endianness   : Little-Endean")
    lines.append(f"Encoding     : UTF-8 (fixed-length)")
    lines.append("")

    header = "| CarID | Plate | Brand | Model | Year | Rate (THB/day) | Status | Rented |"
    sep = "-" * len(header)
    lines += [sep, header, sep]
    for r in rows:
        lines.append(
            f"| {r.car_id:<4} | {r.license_plate:<8} | {r.brand:<7} | {r.model:<7} | "
            f"{r.year:<4} | {r.daily_rate_thb:>13.2f} | {_status(r.status):<7} | {_fmt_yesno(r.is_rented):<3} |"
        )
    lines += [sep, ""]

    total = len(rows)
    active = [r for r in rows if r.status == config.ACTIVE]
    deleted = [r for r in rows if r.status == config.DELETED]
    rented = [r for r in active if r.is_rented]
    available = [r for r in active if not r.is_rented]

    lines.append("Summary (นับเฉพาะสถานะ Active)")
    lines.append(f"- Total Cars (records) : {total}")
    lines.append(f"- Active Cars          : {len(active)}")
    lines.append(f"- Deleted Cars         : {len(deleted)}")
    lines.append(f"- Currently Rented     : {len(rented)}")
    lines.append(f"- Available Now        : {len(available)}")
    lines.append("")

    rates = [float(r.daily_rate_thb) for r in active]
    if rates:
        lines.append("Rate Statistics (THB/day, Active only)")
        lines.append(f"- Min : {min(rates):.2f}")
        lines.append(f"- Max : {max(rates):.2f}")
        lines.append(f"- Avg : {statistics.mean(rates):.2f}")
        lines.append("")

    by_brand: Dict[str, int] = {}
    for r in active:
        by_brand[r.brand] = by_brand.get(r.brand, 0) + 1
    if by_brand:
        lines.append("Cars by Brand (Active only)")
        for b, c in sorted(by_brand.items()):
            lines.append(f"- {b} : {c}")
        lines.append("")

    text = "\n".join(lines)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path
