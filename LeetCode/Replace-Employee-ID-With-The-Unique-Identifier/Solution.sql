1# Write your MySQL query statement below
2SELECT a.unique_id, b.name
3FROM EmployeeUNI a 
4RIGHT JOIN
5Employees b ON b.id = a.id ;