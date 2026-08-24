use ds_sql_practice;

select 'customers' as table_name, count(*) as row_count
from customers

UNION ALL

select 'products', count(*)
from products


UNION ALL

SELECT 'orders', COUNT(*)
FROM orders

UNION ALL

SELECT 'order_items', COUNT(*)
FROM order_items

UNION ALL

SELECT 'payments', COUNT(*)
FROM payments;