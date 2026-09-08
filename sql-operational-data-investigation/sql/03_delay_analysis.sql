-- Delay investigation by warehouse and product category

-- Warehouse exposure: rate and absolute delayed volume
WITH warehouse_metrics AS (
    SELECT
        f.warehouse_id,
        COUNT(*) AS fulfilled_orders,
        SUM(CASE WHEN DATE(f.ship_date) > DATE(o.promised_date) THEN 1 ELSE 0 END) AS delayed_orders
    FROM orders AS o
    JOIN fulfilments AS f ON o.order_id = f.order_id
    GROUP BY f.warehouse_id
)
SELECT
    w.warehouse_name,
    wm.fulfilled_orders,
    wm.delayed_orders,
    ROUND(100.0 * wm.delayed_orders / wm.fulfilled_orders, 2) AS delay_rate_pct
FROM warehouse_metrics AS wm
JOIN warehouses AS w ON wm.warehouse_id = w.warehouse_id
ORDER BY wm.delayed_orders DESC;

-- Product-category exposure
WITH order_delays AS (
    SELECT
        oi.product_id,
        CASE WHEN DATE(f.ship_date) > DATE(o.promised_date) THEN 1 ELSE 0 END AS delayed_flag
    FROM order_items AS oi
    JOIN orders AS o ON oi.order_id = o.order_id
    JOIN fulfilments AS f ON oi.order_id = f.order_id
)
SELECT
    p.product_category,
    COUNT(*) AS order_item_records,
    SUM(od.delayed_flag) AS delayed_records,
    ROUND(100.0 * AVG(od.delayed_flag), 2) AS delay_rate_pct
FROM order_delays AS od
JOIN products AS p ON od.product_id = p.product_id
GROUP BY p.product_category
ORDER BY delayed_records DESC;

-- Average delay duration among delayed orders
SELECT
    w.warehouse_name,
    ROUND(AVG(JULIANDAY(f.ship_date) - JULIANDAY(o.promised_date), 2), 2) AS avg_days_late
FROM orders AS o
JOIN fulfilments AS f ON o.order_id = f.order_id
JOIN warehouses AS w ON f.warehouse_id = w.warehouse_id
WHERE DATE(f.ship_date) > DATE(o.promised_date)
GROUP BY w.warehouse_id, w.warehouse_name
ORDER BY avg_days_late DESC;
