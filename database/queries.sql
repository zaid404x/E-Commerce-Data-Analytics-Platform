-- =====================================================
-- PHASE 1 : Basic queries to get a feel of the data
-- =====================================================

SELECT *
FROM Customers;

SELECT *
FROM Products;

SELECT *
FROM Orders;

SELECT *
FROM Order_Items;

SELECT COUNT(*) AS Total_Customers
FROM Customers;

SELECT COUNT(*) AS Total_Products
FROM Products;

SELECT COUNT(*) AS Total_Orders
FROM Orders;

SELECT ROUND(SUM(total_amount),2) AS Total_Revenue
FROM Orders;

SELECT
order_id,
customer_id,
total_amount
FROM Orders
ORDER BY total_amount DESC
LIMIT 10;

SELECT *
FROM Customers
WHERE city='Mumbai';

SELECT *
FROM Products
WHERE price > 5000;

SELECT DISTINCT category
FROM Products;

SELECT DISTINCT order_status
FROM Orders;
-- =====================================================
-- PHASE 2 : agrregation queries above basic
-- =====================================================

SELECT
order_status,
COUNT(*) AS Total_Orders
FROM Orders
GROUP BY order_status;

SELECT
ROUND(AVG(total_amount),2) AS Average_Order_Value
FROM Orders;

SELECT
MAX(total_amount) AS Highest_Order
FROM Orders;

SELECT
MIN(total_amount) AS Lowest_Order
FROM Orders;

SELECT
category,
COUNT(*) AS Products
FROM Products
GROUP BY category;

SELECT
brand,
COUNT(*) AS Total_Products
FROM Products
GROUP BY brand;

SELECT
city,
COUNT(*) AS Customers
FROM Customers
GROUP BY city
ORDER BY Customers DESC;

SELECT
state,
COUNT(*) AS Customers
FROM Customers
GROUP BY state
ORDER BY Customers DESC;

SELECT
category,
ROUND(AVG(price),2) AS Average_Price
FROM Products
GROUP BY category;

SELECT
customer_id,
SUM(total_amount) AS Total_Spent
FROM Orders
GROUP BY customer_id
ORDER BY Total_Spent DESC;

SELECT
o.order_id,
c.first_name,
c.last_name,
o.order_date,
o.total_amount
FROM Orders o
INNER JOIN Customers c
ON o.customer_id = c.customer_id;

SELECT
p.product_name,
SUM(oi.quantity) AS Quantity_Sold
FROM Products p
INNER JOIN Order_Items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY Quantity_Sold DESC;

SELECT
p.product_name,
ROUND(SUM(oi.line_total),2) AS Revenue
FROM Products p
INNER JOIN Order_Items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY Revenue DESC;


-- =====================================================
-- PHASE 4 : high level  SQL
-- =====================================================



WITH CustomerRevenue AS
(
    SELECT
        customer_id,
        SUM(total_amount) AS Revenue
    FROM Orders
    GROUP BY customer_id
)
SELECT *
FROM CustomerRevenue
ORDER BY Revenue DESC;




SELECT
    order_id,
    customer_id,
    total_amount,
    ROW_NUMBER() OVER(ORDER BY total_amount DESC) AS Row_Number
FROM Orders;




SELECT
    customer_id,
    total_amount,
    RANK() OVER(ORDER BY total_amount DESC) AS Customer_Rank
FROM Orders;



SELECT
    customer_id,
    total_amount,
    DENSE_RANK() OVER(ORDER BY total_amount DESC) AS Dense_Rank
FROM Orders;




SELECT
    order_id,
    order_date,
    total_amount,
    LAG(total_amount) OVER(ORDER BY order_date) AS Previous_Order_Amount
FROM Orders;




SELECT
    order_id,
    order_date,
    total_amount,
    LEAD(total_amount) OVER(ORDER BY order_date) AS Next_Order_Amount
FROM Orders;




SELECT
    order_id,
    order_date,
    total_amount,
    SUM(total_amount)
    OVER(ORDER BY order_date) AS Running_Total
FROM Orders;



SELECT
    customer_id,
    total_amount,
    NTILE(4)
    OVER(ORDER BY total_amount DESC) AS Revenue_Quartile
FROM Orders;




SELECT
    customer_id,
    COUNT(order_id) AS Total_Orders,
    SUM(total_amount) AS Total_Spent,
    CASE
        WHEN SUM(total_amount) >= 100000 THEN 'Premium'
        WHEN SUM(total_amount) >= 50000 THEN 'Regular'
        ELSE 'Occasional'
    END AS Customer_Category
FROM Orders
GROUP BY customer_id
ORDER BY Total_Spent DESC;


-- Top 10 Best Selling Products using CTE

WITH ProductSales AS
(
    SELECT
        product_id,
        SUM(quantity) AS Total_Quantity
    FROM Order_Items
    GROUP BY product_id
)

SELECT
    p.product_id,
    p.product_name,
    p.category,
    ps.Total_Quantity
FROM ProductSales ps
JOIN Products p
ON ps.product_id = p.product_id
ORDER BY ps.Total_Quantity DESC
LIMIT 10;