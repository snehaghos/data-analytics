USE ds_sql_practice;


-- Exercise 21: Orders above the average
-- Find completed orders whose total_amount is greater than the average completed order.

SELECT order_id, customer_id, total_amount
FROM orders
WHERE status='completed'
  AND total_amount > (
      SELECT AVG(total_amount)
      FROM orders
      WHERE status='completed'
  )
ORDER BY total_amount DESC;


-- Exercise 22: Customers above average lifetime revenue
-- Find customers whose completed-order revenue is above the average customer revenue.

WITH customer_revenue AS (
    SELECT customer_id, SUM(total_amount) AS revenue
    FROM orders
    WHERE status='completed'
    GROUP BY customer_id
)
SELECT c.customer_id, c.name, cr.revenue
FROM customer_revenue cr
JOIN customers c ON c.customer_id=cr.customer_id
WHERE cr.revenue > (SELECT AVG(revenue) FROM customer_revenue)
ORDER BY cr.revenue DESC;