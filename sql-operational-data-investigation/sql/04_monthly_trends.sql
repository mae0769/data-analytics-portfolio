-- Monthly fulfilment trend
WITH monthly AS (
    SELECT
        STRFTIME('%Y-%m', o.order_date) AS month,
        COUNT(*) AS fulfilled_orders,
        SUM(CASE WHEN DATE(f.ship_date) > DATE(o.promised_date) THEN 1 ELSE 0 END) AS delayed_orders,
        AVG(JULIANDAY(f.ship_date) - JULIANDAY(o.order_date)) AS avg_fulfilment_days
    FROM orders AS o
    JOIN fulfilments AS f ON o.order_id = f.order_id
    GROUP BY STRFTIME('%Y-%m', o.order_date)
), scored AS (
    SELECT
        month,
        fulfilled_orders,
        delayed_orders,
        ROUND(100.0 * delayed_orders / fulfilled_orders, 2) AS delay_rate_pct,
        ROUND(avg_fulfilment_days, 2) AS avg_fulfilment_days
    FROM monthly
)
SELECT
    month,
    fulfilled_orders,
    delayed_orders,
    delay_rate_pct,
    avg_fulfilment_days,
    LAG(delay_rate_pct) OVER (ORDER BY month) AS previous_month_delay_rate_pct,
    ROUND(
        delay_rate_pct - LAG(delay_rate_pct) OVER (ORDER BY month),
        2
    ) AS month_over_month_change_pct_points,
    ROUND(
        AVG(delay_rate_pct) OVER (
            ORDER BY month
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS three_month_rolling_delay_rate_pct
FROM scored
ORDER BY month;
