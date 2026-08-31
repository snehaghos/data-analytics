USE ds_sql_practice;


-- Exercise 25: Rank customers by revenue
-- Calculate customer revenue and rank customers from highest to lowest.

WITH customer_revenue AS (
    SELECT customer_id, SUM(total_amount) AS revenue
    FROM orders
    WHERE status='completed'
    GROUP BY customer_id
)
SELECT c.name, ROUND(cr.revenue,2) AS revenue,
       DENSE_RANK() OVER (ORDER BY cr.revenue DESC) AS revenue_rank
FROM customer_revenue cr
JOIN customers c ON c.customer_id=cr.customer_id
ORDER BY revenue_rank;


-- Exercise 26: Running monthly revenue
-- Calculate monthly revenue and cumulative revenue across months.

WITH monthly_sales AS (
    SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
           SUM(total_amount) AS revenue
    FROM orders
    WHERE status='completed'
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT month, ROUND(revenue,2) AS revenue,
       ROUND(SUM(revenue) OVER (ORDER BY month),2) AS cumulative_revenue
FROM monthly_sales
ORDER BY month;


-- Exercise 27: Top product per category
-- Rank products within each category by completed revenue and return the top product in each category.

WITH product_sales AS (
    SELECT p.product_id, p.product_name, p.category_id,
           SUM(oi.line_total) AS revenue
    FROM order_items oi
    JOIN orders o ON o.order_id=oi.order_id
    JOIN products p ON p.product_id=oi.product_id
    WHERE o.status='completed'
    GROUP BY p.product_id, p.product_name, p.category_id
), ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY category_id ORDER BY revenue DESC) AS rn
    FROM product_sales
)
SELECT c.category_name, r.product_name, ROUND(r.revenue,2) AS revenue
FROM ranked r
JOIN categories c ON c.category_id=r.category_id
WHERE r.rn=1
ORDER BY c.category_name;