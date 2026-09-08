-- Consolidated investigation view
-- Combines warehouse delay incidence, delayed volume and average days late.

WITH metrics AS (
    SELECT
        f.warehouse_id,
        COUNT(*) AS fulfilled_orders,
        SUM(CASE WHEN DATE(f.ship_date) > DATE(o.promised_date) THEN 1 ELSE 0 END) AS delayed_orders,
        AVG(
            CASE
                WHEN DATE(f.ship_date) > DATE(o.promised_date)
                THEN JULIANDAY(f.ship_date) - JULIANDAY(o.promised_date)
            END
        ) AS avg_days_late_when_delayed
    FROM orders AS o
    JOIN fulfilments AS f ON o.order_id = f.order_id
    GROUP BY f.warehouse_id
)
SELECT
    w.warehouse_name,
    m.fulfilled_orders,
    m.delayed_orders,
    ROUND(100.0 * m.delayed_orders / m.fulfilled_orders, 2) AS delay_rate_pct,
    ROUND(m.avg_days_late_when_delayed, 2) AS avg_days_late_when_delayed,
    RANK() OVER (ORDER BY m.delayed_orders DESC) AS delayed_volume_rank,
    RANK() OVER (ORDER BY 100.0 * m.delayed_orders / m.fulfilled_orders DESC) AS delay_rate_rank
FROM metrics AS m
JOIN warehouses AS w ON m.warehouse_id = w.warehouse_id
ORDER BY delayed_volume_rank;
