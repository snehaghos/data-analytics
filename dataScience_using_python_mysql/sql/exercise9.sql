USE ds_sql_practice;


-- Exercise 23: Monthly revenue trend
-- Calculate completed monthly revenue using a CTE and then sort by revenue descending.

WITH monthly_sales AS (
    SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
           SUM(total_amount) AS revenue
    FROM orders
    WHERE status='completed'
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT month, ROUND(revenue,2) AS revenue
FROM monthly_sales
ORDER BY revenue DESC;


-- Exercise 24: Top 5 customers by revenue
-- Use a CTE to calculate customer revenue and then return the top five customers.

WITH customer_revenue AS (
    SELECT customer_id, SUM(total_amount) AS revenue
    FROM orders
    WHERE status='completed'
    GROUP BY customer_id
)
SELECT c.name, ROUND(cr.revenue,2) AS revenue
FROM customer_revenue cr
JOIN customers c ON c.customer_id=cr.customer_id
ORDER BY cr.revenue DESC
LIMIT 5;