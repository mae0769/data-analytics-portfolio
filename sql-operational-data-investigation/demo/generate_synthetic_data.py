"""Generate an independent synthetic relational dataset for the SQL portfolio demo."""

from pathlib import Path
import sqlite3

import numpy as np
import pandas as pd

SEED = 42
OUT_DIR = Path(__file__).parents[1] / "generated"
DB_PATH = OUT_DIR / "operational_demo.sqlite"


def build_data():
    rng = np.random.default_rng(SEED)

    customers = pd.DataFrame({
        "customer_id": np.arange(1, 101),
        "customer_segment": rng.choice(["Retail", "SME", "Enterprise"], 100, p=[0.50, 0.35, 0.15]),
        "region": rng.choice(["North", "Central", "South"], 100),
    })

    products = pd.DataFrame({
        "product_id": np.arange(1, 31),
        "product_category": rng.choice(["Components", "Consumables", "Equipment", "Packaging", "Maintenance"], 30),
        "unit_price": np.round(rng.uniform(15, 850, 30), 2),
    })

    warehouses = pd.DataFrame({
        "warehouse_id": np.arange(1, 6),
        "warehouse_name": ["Warehouse A", "Warehouse B", "Warehouse C", "Warehouse D", "Warehouse E"],
        "region": ["North", "Central", "South", "Central", "North"],
        "capacity_units": [12000, 15000, 10000, 9000, 13000],
    })

    n_orders = 3000
    start = pd.Timestamp("2025-01-01")
    order_dates = start + pd.to_timedelta(rng.integers(0, 365, n_orders), unit="D")
    promised_days = rng.integers(2, 8, n_orders)

    orders = pd.DataFrame({
        "order_id": np.arange(1, n_orders + 1),
        "customer_id": rng.integers(1, 101, n_orders),
        "order_date": order_dates,
        "promised_date": order_dates + pd.to_timedelta(promised_days, unit="D"),
    })

    items_per_order = rng.integers(1, 4, n_orders)
    order_items = []
    item_id = 1
    for order_id, count in zip(orders["order_id"], items_per_order):
        for _ in range(count):
            order_items.append((item_id, order_id, int(rng.integers(1, 31)), int(rng.integers(1, 25))))
            item_id += 1
    order_items = pd.DataFrame(order_items, columns=["order_item_id", "order_id", "product_id", "quantity"])

    warehouse = rng.integers(1, 6, n_orders)
    base_processing = rng.integers(1, 6, n_orders)
    warehouse_penalty = np.where(warehouse == 4, 2, 0)  # synthetic concentration for investigation
    processing_days = base_processing + warehouse_penalty
    pick_dates = order_dates + pd.to_timedelta(np.maximum(1, processing_days - 1), unit="D")
    late_tail = rng.random(n_orders) < np.where(warehouse == 4, 0.22, 0.08)
    extra_days = np.where(late_tail, rng.integers(1, 5, n_orders), 0)
    ship_dates = pick_dates + pd.to_timedelta(1 + extra_days, unit="D")

    fulfilments = pd.DataFrame({
        "fulfilment_id": np.arange(1, n_orders + 1),
        "order_id": orders["order_id"],
        "warehouse_id": warehouse,
        "pick_date": pick_dates,
        "ship_date": ship_dates,
    })

    return customers, products, warehouses, orders, order_items, fulfilments


def main():
    OUT_DIR.mkdir(exist_ok=True)
    tables = build_data()
    names = ["customers", "products", "warehouses", "orders", "order_items", "fulfilments"]

    with sqlite3.connect(DB_PATH) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)

    print(f"Created synthetic SQLite database: {DB_PATH}")
    print("Seed:", SEED)
    print("Generated records:", len(tables[3]), "orders and", len(tables[4]), "order-item records")


if __name__ == "__main__":
    main()
