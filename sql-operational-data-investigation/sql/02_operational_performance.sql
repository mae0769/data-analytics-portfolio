-- Baseline operational performance

WITH order_status AS (
    SELECT
        o.order_id,
        o.promised_date,
        f.ship_date,
        CASE
            WHEN DATE(f.ship_date) > DATE(o.promised_date) THEN 1
            ELSE 0
        END AS delayed_flag,
        CAST(JULIANDAY(f.ship_date) - JULIANDAY(o.order_date) AS INTEGER) AS fulfilment_days
    FROM orders AS o
    JOIN fulfilments AS f ON o.order_id = f.order_id
)
SELECT
    COUNT(*) AS fulfilled_orders,
    SUM(delayed_flag) AS delayed_orders,
    ROUND(100.0 * AVG(delayed_flag), 2) AS delay_rate_pct,
    ROUND(AVG(fulfilment_days), 2) AS average_fulfilment_days
FROM order_status;

-- Performance by warehouse
WITH order_status AS (
    SELECT
        f.warehouse_id,
        CASE WHEN DATE(f.ship_date) > DATE(o.promised_date) THEN 1 ELSE 0 END AS delayed_flag,
        CAST(JULIANDAY(f.ship_date) - JULIANDAY(o.order_date) AS INTEGER) AS fulfilment_days
    FROM orders AS o
    JOIN fulfilments AS f ON o.order_id = f.order_id
)
SELECT
    w.warehouse_name,
    COUNT(*) AS fulfilled_orders,
    SUM(os.delayed_flag) AS delayed_orders,
    ROUND(100.0 * AVG(os.delayed_flag), 2) AS delay_rate_pct,
    ROUND(AVG(os.fulfilment_days), 2) AS average_fulfilment_days
FROM order_status AS os
JOIN warehouses AS w ON os.warehouse_id = w.warehouse_id
GROUP BY w.warehouse_id, w.warehouse_name
ORDER BY delay_rate_pct DESC;
