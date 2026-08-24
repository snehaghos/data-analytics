USE ds_sql_practice;


-- SELECT product_name,
--        unit_price,
--        ROUND(unit_price * 1.18, 2) AS price_with_tax
-- FROM products;


-- SELECT order_id,
--        total_amount,
--        CASE
--            WHEN total_amount >= 3000 THEN 'High Value'
--            WHEN total_amount >= 1500 THEN 'Medium Value'
--            ELSE 'Low Value'
--        END AS order_segment
-- FROM orders;


-- SELECT order_id,
--        total_amount,
--        CASE
--            WHEN total_amount >= 3000 THEN 'High'
--            WHEN total_amount >= 1500 THEN 'Medium'
--            ELSE 'Low'
--        END AS value_band
-- FROM orders
-- ORDER BY total_amount DESC;


-- SELECT order_id,
--        order_date,
--        YEAR(order_date) AS order_year,
--        MONTH(order_date) AS month_number,
--        DATE_FORMAT(order_date, '%Y-%m') AS order_month
-- FROM orders
-- ORDER BY order_date;




SELECT customer_id,
       UPPER(name) AS customer_name_upper,
       LOWER(email) AS email_lower
FROM customers;