USE ds_sql_practice;


-- Exercise 9: Overall business summary
-- For completed orders, calculate order count, revenue, average order value, minimum and maximum order value.

SELECT COUNT(*) AS order_count,
       ROUND(SUM(total_amount),2) AS revenue,
       ROUND(AVG(total_amount),2) AS avg_order_value,
       ROUND(MIN(total_amount),2) AS min_order,
       ROUND(MAX(total_amount),2) AS max_order
FROM orders
WHERE status='completed';


-- Exercise 10: Count by status
-- Count orders in each status and calculate the percentage of all orders for each status.

SELECT status,
       COUNT(*) AS order_count,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM orders), 2) AS pct_of_orders
FROM orders
GROUP BY status
ORDER BY order_count DESC;


-- Exercise 11: Daily revenue
-- For completed orders, show revenue by order date.

SELECT order_date,
       COUNT(*) AS orders,
       ROUND(SUM(total_amount),2) AS revenue
FROM orders
WHERE status='completed'
GROUP BY order_date
ORDER BY order_date;