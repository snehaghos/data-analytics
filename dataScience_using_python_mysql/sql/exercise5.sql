USE ds_sql_practice;


-- Exercise 12: Revenue by customer city
-- Find completed-order revenue and order count by city.

SELECT c.city,
       COUNT(o.order_id) AS order_count,
       ROUND(SUM(o.total_amount),2) AS revenue
FROM customers c
JOIN orders o ON o.customer_id=c.customer_id
WHERE o.status='completed'
GROUP BY c.city
ORDER BY revenue DESC;


-- Exercise 13: Customers with many completed orders
-- Find customers with at least 3 completed orders.

SELECT c.customer_id, c.name,
       COUNT(o.order_id) AS completed_orders
FROM customers c
JOIN orders o ON o.customer_id=c.customer_id
WHERE o.status='completed'
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) >= 3
ORDER BY completed_orders DESC;