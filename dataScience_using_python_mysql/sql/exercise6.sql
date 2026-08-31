USE ds_sql_practice;


-- Exercise 14: Join orders to customers
-- Return order_id, customer name, city, order date, and total amount for completed orders.

SELECT o.order_id, c.name, c.city, o.order_date, o.total_amount
FROM orders o
JOIN customers c ON c.customer_id=o.customer_id
WHERE o.status='completed'
ORDER BY o.order_date;


-- Exercise 15: Join products to categories
-- List every product with its category name and price.

SELECT p.product_id, p.product_name, c.category_name, p.unit_price
FROM products p
JOIN categories c ON c.category_id=p.category_id
ORDER BY c.category_name, p.product_name;


-- Exercise 16: Join order line items
-- Return each completed order item with customer name, product name, quantity, and line total.

SELECT o.order_id, c.name AS customer_name, p.product_name,
       oi.quantity, oi.unit_price, oi.line_total
FROM orders o
JOIN customers c ON c.customer_id=o.customer_id
JOIN order_items oi ON oi.order_id=o.order_id
JOIN products p ON p.product_id=oi.product_id
WHERE o.status='completed'
ORDER BY o.order_id, oi.order_item_id;


-- Exercise 17: LEFT JOIN: customers with no completed orders
-- List all customers, including customers who have never placed a completed order.

SELECT c.customer_id, c.name,
       COUNT(o.order_id) AS completed_orders
FROM customers c
LEFT JOIN orders o
  ON o.customer_id=c.customer_id
 AND o.status='completed'
GROUP BY c.customer_id, c.name
ORDER BY completed_orders, c.name;

