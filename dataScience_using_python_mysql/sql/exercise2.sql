
-- SELECT order_id, customer_id, order_date, status, total_amount
-- FROM orders
-- LIMIT 10;

-- SELECT order_id, order_date, total_amount
-- FROM orders
-- WHERE status = 'completed';


-- SELECT DISTINCT city
-- FROM customers
-- ORDER BY city;

-- SELECT order_id, customer_id, total_amount
-- FROM orders
-- WHERE total_amount > 3000
-- ORDER BY total_amount DESC;



-- SELECT customer_id, name, city
-- FROM customers
-- WHERE city IN ('Kolkata', 'Delhi', 'Mumbai')
-- ORDER BY city, name;



-- SELECT customer_id, name
-- FROM customers
-- WHERE name LIKE 'A%';

-- SELECT customer_id, name
-- FROM customers
-- WHERE name LIKE '%a%';


SELECT product_id, product_name, unit_price
FROM products
WHERE unit_price BETWEEN 700 AND 2000
ORDER BY unit_price;

 
