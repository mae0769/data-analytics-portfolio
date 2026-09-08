-- Data-quality checks
-- These checks are intended to run after loading the synthetic tables.

-- 1. Duplicate order IDs
SELECT order_id, COUNT(*) AS row_count
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;

-- 2. Orders without a fulfilment record
SELECT o.order_id
FROM orders AS o
LEFT JOIN fulfilments AS f ON o.order_id = f.order_id
WHERE f.order_id IS NULL;

-- 3. Missing warehouse assignments
SELECT fulfilment_id, order_id
FROM fulfilments
WHERE warehouse_id IS NULL;

-- 4. Fulfilment activity before the order was placed
SELECT fulfilment_id, order_id, pick_date, ship_date, order_date
FROM fulfilments AS f
JOIN orders AS o ON f.order_id = o.order_id
WHERE DATE(f.pick_date) < DATE(o.order_date);

-- 5. Shipments after the promised date
SELECT fulfilment_id, order_id, ship_date, promised_date
FROM fulfilments AS f
JOIN orders AS o ON f.order_id = o.order_id
WHERE DATE(f.ship_date) > DATE(o.promised_date);

-- 6. Invalid order quantities
SELECT order_item_id, order_id, product_id, quantity
FROM order_items
WHERE quantity <= 0;
