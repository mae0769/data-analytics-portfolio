PRAGMA foreign_keys = ON;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_segment TEXT NOT NULL,
    region TEXT NOT NULL
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_category TEXT NOT NULL,
    unit_price REAL NOT NULL CHECK (unit_price > 0)
);

CREATE TABLE warehouses (
    warehouse_id INTEGER PRIMARY KEY,
    warehouse_name TEXT NOT NULL,
    region TEXT NOT NULL,
    capacity_units INTEGER NOT NULL CHECK (capacity_units > 0)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    promised_date TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE fulfilments (
    fulfilment_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    warehouse_id INTEGER NOT NULL,
    pick_date TEXT NOT NULL,
    ship_date TEXT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);
