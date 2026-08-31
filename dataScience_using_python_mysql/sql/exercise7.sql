USE ds_sql_practice;


-- Exercise 18: Revenue by product
-- Calculate completed revenue per product using order_items.
-- Return product name, units sold, and revenue.

SELECT p.product_id, p.product_name,
       SUM(oi.quantity) AS units_sold,
       ROUND(SUM(oi.line_total),2) AS revenue
FROM order_items oi
JOIN orders o ON o.order_id=oi.order_id
JOIN products p ON p.product_id=oi.product_id
WHERE o.status='completed'
GROUP BY p.product_id, p.product_name
ORDER BY revenue DESC;


-- Exercise 19: Revenue by category
-- Calculate units sold and revenue by product category.

SELECT c.category_name,
       SUM(oi.quantity) AS units_sold,
       ROUND(SUM(oi.line_total),2) AS revenue
FROM order_items oi
JOIN orders o ON o.order_id=oi.order_id
JOIN products p ON p.product_id=oi.product_id
JOIN categories c ON c.category_id=p.category_id
WHERE o.status='completed'
GROUP BY c.category_id, c.category_name
ORDER BY revenue DESC;


-- Exercise 20: Customer lifetime revenue
-- For completed orders, calculate total revenue, number of orders, and average order value per customer.

SELECT c.customer_id, c.name,
       COUNT(o.order_id) AS order_count,
       ROUND(SUM(o.total_amount),2) AS lifetime_revenue,
       ROUND(AVG(o.total_amount),2) AS avg_order_value
FROM customers c
JOIN orders o ON o.customer_id=c.customer_id
WHERE o.status='completed'
GROUP BY c.customer_id, c.name
ORDER BY lifetime_revenue DESC;