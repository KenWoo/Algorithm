SELECT [Name] Customers
FROM [Customers] 
WHERE Customers.id NOT IN
(SELECT customerid FROM Orders)